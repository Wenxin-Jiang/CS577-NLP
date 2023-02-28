import pandas as pd
import numpy as np

from loguru import logger


def sigmoid(x: float):
    # Logistic regression function (Sigmoid)
    output = 1 / (1 + np.exp(-x))
    return output


def read_csv(path: str) -> pd.DataFrame:
    file = pd.read_csv(path)
    return file


def loss_lr(pred, gt):

    return


def feature_rep(train_set, test_set):
    # Create feature representations for data
    word2vec = {}
    word_set = {}
    word_all = []
    idx = 0
    # logger.debug(train_set)
    for dataset in (train_set, test_set):
        for text in dataset.text:
            words = text.split()
            for word in words:
                if word not in word2vec:
                    word_all.append(word)
                    word2vec[word] = idx
                    idx += 1
        word_set = set(word_all)
        # logger.debug(idx)
    logger.info(len(word2vec))
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
    logger.info(len(text_features[0]))
    logger.info(len(text_features))
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

def pre_processing(train_set: pd.DataFrame, test_set: pd.DataFrame):
    train_set = data_cleaning(train_set)
    test_set = data_cleaning(test_set)
    logger.info(f"After data cleaning, len(train_set) is {len(train_set)}, len(test_set) is {len(test_set)}")
    embedding = feature_rep(train_set, test_set)
    
    # Create trianing and testing inputs
    text_features_train = text_features(train_set, embedding)
    text_features_test = text_features(test_set, embedding)
    
    # Create labels
    emotions = [_ for _ in train_set.emotions]

    emotion_set = set(emotions)

    emotion2int = {emotion: i for i, emotion in enumerate(emotion_set)}
    int2emotion = {i: emotion for i, emotion in enumerate(emotion_set)}
    
    emotions = [emotion2int[emotion] for emotion in emotions]
    train_targets = np.zeros((len(emotions), len(emotion_set)))
    for i, emotion in enumerate(emotions):
        train_targets[i, emotion] = 1
    # TODO: Data cleaning
    return embedding, text_features_train, text_features_test,\
        emotion_set, train_targets, emotion2int, int2emotion


def post_processing(test_set, pred_emotions):
    output = test_set.copy()
    output['emotions'] = pred_emotions
    output.to_csv("./test_lr.csv")
    return output

def LR():
    TRAIN_PATH = "./train.csv"
    TEST_PATH = "./test.csv"
    train_set = read_csv(TRAIN_PATH)
    test_set = read_csv(TEST_PATH)

    embedding, text_features_train, text_features_test,\
          emotion_set, train_targets, emotion2int, int2emotion = pre_processing(train_set, test_set)
    # your logistic regression 
    weights = np.zeros((len(embedding), len(emotion_set)))
    learning_rate = 0.01
    num_epochs = 100
    for epoch in range(num_epochs):
        scores = np.dot(np.array(text_features_train), weights)
        # Logistic regression function (Sigmoid)
        predictions = sigmoid(scores)
        # logger.debug(np.array(predictions).shape)
        # logger.debug(np.array(train_targets).shape)
        error = train_targets - predictions
        gradient = np.dot(np.array(text_features_train).T, error)
        weights += learning_rate * gradient
        logger.info(f"Epoch = {epoch}")

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
    logger.debug(pred_emotion)
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