import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from loguru import logger


def sigmoid(x: float):
    # Logistic regression function (Sigmoid)
    output = 1 / (1 + np.exp(-x))
    return output


def softmax(x):
    ex = np.exp(x - np.max(x))
    return ex/ex.sum()

def read_csv(path: str) -> pd.DataFrame:
    file = pd.read_csv(path)
    return file


def loss_lr(pred, gt):

    return


def feature_rep(train_set, val_set, test_set):
    # Create feature representations for data
    word2vec = {}
    word_set = {}
    word_all = []
    idx = 0
    # logger.debug(train_set)
    for dataset in (train_set, val_set, test_set):
        for text in dataset.text:
            words = text.split()
            for word in words:
                if word not in word2vec:
                    word_all.append(word)
                    word2vec[word] = idx
                    idx += 1
        word_set = set(word_all)
        # logger.debug(idx)
    # logger.info(len(word2vec))
    # logger.info(len(word_set))
        # print(text)
        # break
    return word2vec


def text_features(dataset, embedding):
    text_features = []
    for text in dataset.text:
        features = [0] * len(embedding)
        words = text.split()
        for word in words:
            features[embedding[word]] = 1
        text_features.append(features)
    # logger.info(len(text_features[0]))
    # logger.info(len(text_features))
    return text_features


def data_cleaning(dataset: pd.DataFrame) -> None:
    '''
        Clean the duplicated entries
    '''
    dataset = dataset.sort_values("id")
    dataset_dup = dataset.duplicated(subset=["id"])
    index = np.where(dataset_dup==True)
    dataset = dataset.drop(index[0])
    return dataset


def data_loading(epoch, num_epochs):
    # Load raw dataset
    TRAIN_PATH = "./train.csv"
    TEST_PATH = "./test.csv"
    train_set = read_csv(TRAIN_PATH)
    test_set = read_csv(TEST_PATH)
    
    # data cleaning
    train_set = data_cleaning(train_set)
    test_set = data_cleaning(test_set)
    # logger.info(f"After data cleaning, len(train_set) is {len(train_set)}, len(test_set) is {len(test_set)}")

    # Cross validation
    df_shuffle = train_set.sample(frac=1)
    # logger.info(len(df_shuffle))
    df_size = len(df_shuffle)
    idx_split_left = df_size//num_epochs * (epoch)
    idx_split_right = df_size//num_epochs * (epoch+1)
    train_set = pd.concat([df_shuffle.iloc[:idx_split_left], df_shuffle.iloc[idx_split_right:]])
    val_set = df_shuffle.iloc[idx_split_left:idx_split_right]
    return train_set, val_set, test_set

def pre_processing(train_set: pd.DataFrame, val_set: pd.DataFrame, test_set: pd.DataFrame):
    
    embedding = feature_rep(train_set, val_set, test_set)
    # Create trianing and testing inputs
    text_features_train = text_features(train_set, embedding)
    text_features_val = text_features(val_set, embedding)
    text_features_test = text_features(test_set, embedding)
    
    # Create labels
    emotions_train = [_ for _ in train_set.emotions]
    emotions_val = [_ for _ in val_set.emotions]

    emotion_set = set(emotions_train)

    emotion2int = {emotion: i for i, emotion in enumerate(emotion_set)}
    int2emotion = {i: emotion for i, emotion in enumerate(emotion_set)}
    
    emotions_train = [emotion2int[emotion] for emotion in emotions_train]
    emotions_val = [emotion2int[emotion] for emotion in emotions_val]
    train_targets = np.zeros((len(emotions_train), len(emotion_set)))
    val_targets = np.zeros((len(emotions_val), len(emotion_set)))
    for i, emotion in enumerate(emotions_train):
        train_targets[i, emotion] = 1
    for i, emotion in enumerate(emotions_val):
        val_targets[i, emotion] = 1

    return embedding, text_features_train, text_features_val, text_features_test,\
        emotion_set, train_targets, val_targets, emotion2int, int2emotion


def post_processing(test_set, pred_emotions):
    output = test_set.copy()
    output['emotions'] = pred_emotions
    output.to_csv("./test_lr.csv")
    return output

def LR():
    
    # Load raw dataset
    TRAIN_PATH = "./train.csv"
    TEST_PATH = "./test.csv"
    train_set = read_csv(TRAIN_PATH)
    test_set = read_csv(TEST_PATH)
    val_set = read_csv(TRAIN_PATH)
    train_set = data_cleaning(train_set)
    val_set = data_cleaning(val_set)
    test_set = data_cleaning(test_set)
    embedding, _, _, text_features_test,\
          emotion_set, _, _, emotion2int, int2emotion = pre_processing(train_set, val_set, test_set)
    # your logistic regression 
    weights = np.zeros((len(embedding), len(emotion_set)))
    learning_rate = 0.01
    num_epochs = 10

    errors_train = []
    errors_val = []
    
    
    for epoch in range(num_epochs):
        # Cross validation
        train_set, val_set, test_set = data_loading(epoch, num_epochs)
        _, text_features_train, text_features_val, _,\
          _, train_targets, val_targets, _, _ = pre_processing(train_set, val_set, test_set)
        # text_features_train = text_features(train_set, embedding)
        # text_features_val = text_features(val_set, embedding)
        # text_features_test = text_features(test_set, embedding)


        output = np.dot(np.array(text_features_train), weights)
        # Logistic regression function (Sigmoid)
        predictions = sigmoid(output)
        # logger.debug(np.array(predictions).shape)
        # logger.debug(np.array(train_targets).shape)
        error = train_targets - predictions
        errors_train.append(error)
        gradient = np.dot(np.array(text_features_train).T, error)
        weights += learning_rate * gradient
        
           
        # evaluation on val_set
        pred_val = sigmoid(np.dot(np.array(text_features_val), weights))
        error_val = val_targets - pred_val
        # logger.debug(pred_val.shape)
        # logger.debug(val_targets.shape)
        # largest_idx = np.argmax(pred_val)
        # pred = np.eye(pred_val.shape[1])[np.argmax(pred_val, axis=1)]
        # logger.debug(pred)
        # pred[largest_idx] = 1
        errors_val.append(error_val)


        predictions = 1 / (1 + np.exp(-pred_val))
        predictions = np.round(predictions)
        predicted_emotion = int2emotion[np.argmax(predictions[0])]
        val_emotions = int2emotion[np.argmax(val_targets)]
        score = np.sum(predicted_emotion==val_emotions) / len(val_targets)
        logger.info(f"Epoch {epoch}: Accuracy = {score * 100}%")
        # break
    logger.debug(errors_train)
    logger.debug(errors_val)

    # Predict emotions for the test data
    scores = np.dot(text_features_test, weights)
    predictions = 1 / (1 + np.exp(-scores))
    predictions = np.round(predictions)
    predicted_emotion = int2emotion[np.argmax(predictions[0])]
    # logger.debug(predicted_emotion)
    
    pred_emotion = []

    scores = np.dot(text_features_test, weights)
    predictions = 1 / (1 + np.exp(-scores))
    # logger.debug(predictions)
    # predictions = np.ones(predictions.shape) * np.argmax(predictions, axis=1)
    # len(np.argmax(predictions, axis=1))
    pred = np.zeros(predictions.shape)
    for idx in range(pred.shape[0]):
        # logger.debug(np.argmax(predictions, axis=1)[idx])
        pred[idx][np.argmax(predictions, axis=1)[idx]] = 1

    for idx in range(pred.shape[0]):
        # logger.debug(np.where(pred[idx]==1))
        
        # logger.debug(int_to_emotion[np.where(pred[idx]==1)[0][0]])
        pred_emotion.append(int2emotion[np.where(pred[idx]==1)[0][0]])
    # predictions = np.argmax(predictions)
    # predicted_emotion = int_to_emotion[np.argmax(predictions[0])]
    # logger.debug(pred_emotion)
    output = post_processing(test_set, pred_emotion)
    
    return


def NN():

    # your Multi-layer Neural Network
    pass


if __name__ == '__main__':
    print ("..................Beginning of Logistic Regression................")
    LR()
    print ("..................End of Logistic Regression................")

    print("------------------------------------------------")

    print ("..................Beginning of Neural Network................")
    NN()
    print ("..................End of Neural Network................")