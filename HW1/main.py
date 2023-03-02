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



def feature_rep(train_set, val_set):
    # Create feature representations for data
    word2vec = {}
    word_set = {}
    word_all = []
    idx = 0
    # logger.debug(train_set)
    for dataset in (train_set, val_set):
        for text in dataset.text:
            words = text.split()
            for word in words:
                if word not in word2vec:
                    word_all.append(word)
                    word2vec[word] = idx
                    idx += 1
        word_set = set(word_all)
        # logger.debug(idx)
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
            try: 
                features[embedding[word]] = 1
            except:
                continue
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
    
    embedding = feature_rep(train_set, val_set)
    logger.info(f"Size of vocabulary = {len(embedding)}")
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
    # TODO: LR vs. Accuracy
    learning_rate = 0.1
    num_iters = 120
    reg_lambda = 0.001
    folds = 5

    errors_train = []
    errors_val = []

    # weights = np.zeros((len(embedding), len(emotion_set)))
    best_score = 0
    score_arr = []
    for fold in range(folds):
        train_set, val_set, test_set = data_loading(fold, folds)
        _, text_features_train, text_features_val, _,\
                _, train_targets, val_targets, _, _ = pre_processing(train_set, val_set, test_set)
        weights = np.zeros((len(embedding), len(emotion_set)))
        if fold == 0:
            logger.info(f"Input size = {np.array(text_features_train).shape}")
        scores = []
        for iter in range(num_iters):
            # Cross validation
            
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
            gradient = np.dot(np.array(text_features_train).T, error) + reg_lambda * weights
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
            
            predictions = sigmoid(pred_val)
            # predictions = 1 / (1 + np.exp(-pred_val))
            # logger.debug(predictions)
            largest_idx = np.argmax(predictions, axis=1)
            # logger.debug(largest_idx)
            val_pred = np.eye(predictions.shape[1])[largest_idx]
            # logger.debug(np.argmax(val_pred))
            # =============
            # predicted_emotions = []
            # for pred_emotion in np.argmax(val_pred, axis=1):      
            #     predicted_emotions.append(int2emotion[pred_emotion])

            # val_emotions = []
            # for val_emotion in np.argmax(val_targets, axis=1):
            #     val_emotions.append(int2emotion[val_emotion])
            # # val_emotions = int2emotion[np.argmax(val_targets, axis=1)]
            # # logger.debug(predicted_emotions)
            # # logger.debug(val_emotions)
            # count = 0
            # for i in range(len(predicted_emotions)):
            #     if predicted_emotions[i] == val_emotions[i]:
            #         count += 1
            # =============
            score = np.mean(\
                np.argmax(val_pred, axis=1) == \
                    np.argmax(val_targets, axis=1))
            # score = count / len(val_targets)
            scores.append(score)
            # if score > 0:
                # logger.debug(predicted_emotion)
            logger.info(f"Iteration {iter}: Accuracy = {score * 100:.2f}%")
            # break
        if score == 0 or score > best_score:
            best_weights = weights
            best_score = score
        score_arr.append(scores)
        logger.info(f"Best Accuracy = {best_score * 100:.2f}%")
    # logger.info(f"Input size = {np.array(text_features_train).shape}")
    for scores in score_arr:
        plt.plot(np.arange(len(scores)), scores)
        plt.title(f"LR: {folds}-fold Cross Validation, lr={learning_rate}, lambda={reg_lambda}, iteration={num_iters}, highest acc={best_score}")
    plt.xlabel("Iteration")
    plt.ylabel("Validation Accuracy")
    plt.savefig(f"LR_highestAcc={best_score}_{folds}-fold Cross Validation_lr={learning_rate}_lambda={reg_lambda}_iteration={num_iters}.png")


    # Predict test data and save results into csv file
    pred_test = sigmoid(np.dot(np.array(text_features_test), best_weights))

    predictions = sigmoid(pred_test)
    largest_idx = np.argmax(predictions, axis=1)
    # logger.debug(largest_idx)
    test_pred = np.eye(predictions.shape[1])[largest_idx]
    # logger.debug(np.argmax(val_pred))
    predicted_emotions = []
    for pred_emotion in np.argmax(test_pred, axis=1):      
        predicted_emotions.append(int2emotion[pred_emotion])

    test_set['emotions'] = predicted_emotions
    test_set.to_csv("./test_lg.csv")
    logger.info(f"Saving test results...")
    return


class NeuralNetwork:
    # Reference: https://pylessons.com/Neural-network-single-layer-part3
    # Reference: https://towardsai.net/p/machine-learning/nothing-but-numpy-understanding-creating-neural-networks-with-computational-graphs-from-scratch-6299901091b0
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        # logger.debug(f"W1: {self.W1.shape}")
        self.b1 = np.zeros((1, hidden_size))
        # logger.debug(f"b1: {self.b1.shape}")
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        # logger.debug(f"W2: {self.W2.shape}")
        self.b2 = np.zeros((1, output_size))
        # logger.debug(f"b2: {self.b2.shape}")
        self.scores = []
    def forward(self, X):
        # logger.debug(X.shape)
        # logger.debug(self.W1.shape)
        self.z1 = np.dot(X, self.W1) + self.b1
        # logger.debug(f"z1: {self.z1.shape}")
        # self.a1 = np.tanh(self.z1)
        # Use ReLU instead
        self.a1 = np.maximum(0, self.z1)
        # logger.debug(self.W2.shape)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        exp_scores = np.exp(self.z2 - np.max(self.z2))
        self.probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        return self.probs
    
        
    def backward(self, X, y, y_hat, learning_rate):
        # logger.debug(f"X.shape={X.shape}, y.shape={y.shape}, y_hat.shape={y_hat.shape}")
        delta2 = y_hat
        delta2[range(len(X)), np.argmax(y, axis=1)] -= 1
        # logger.debug(self.W2.shape)
        # logger.debug(self.z1.shape)
        delta1 = delta2.dot(self.W2.T) * (1 - np.power(np.tanh(self.z1), 2))
        
        dW2 = np.dot(self.a1.T, delta2)
        db2 = np.sum(delta2, axis=0, keepdims=True)
        dW1 = np.dot(X.T, delta1)
        db1 = np.sum(delta1, axis=0)

        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1

    def train(self, X, y, val_targets, text_features_val, num_epochs, learning_rate):
        for epoch in range(num_epochs):
            # forward pass
            y_hat = self.forward(X)
            # calculate the loss
            correct_logprobs = -np.log(y_hat[range(len(X)), np.argmax(y, axis=1)]+1e-12)
            data_loss = np.sum(correct_logprobs) / len(X)
            # print the loss every 100 epochs
            

                # self.scores.append(score)
            # backward pass
            # logger.debug(X.shape)
            # logger.debug(y.shape)
            self.backward(X, y, y_hat, learning_rate)
            if epoch % 50 == 0:
                score = np.mean(self.predict(text_features_val) == np.argmax(val_targets, axis=1))
                self.scores.append(score)
                logger.info(f"Epoch: {epoch}, loss: {data_loss}, accuracy: {score * 100:.2f}%.")

            # eval

            
            
    def predict(self, X):
        # forward pass
        y_hat = self.forward(X)
        # return the index with highest probability
        return np.argmax(y_hat, axis=1)


    def get_scores(self):
        return self.scores
    
def NN():
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
    
    folds = 5
    scores = []
    best_score = 0
    for fold in range(folds):
        train_set, val_set, test_set = data_loading(fold, folds)
        _, text_features_train, text_features_val, _,\
                _, train_targets, val_targets, _, _ = pre_processing(train_set, val_set, test_set)
        weights = np.zeros((len(embedding), len(emotion_set)))
        if fold == 0:
            logger.info(f"Input size = {np.array(text_features_train).shape}")
        text_features_train = np.array(text_features_train)
        train_targets = np.array(train_targets)
        text_features_val = np.array(text_features_val)
        val_targets = np.array(val_targets)
        X = np.array(text_features_train)
        y = np.array(train_targets)
        # create a neural network with 100 hidden units
        nn = NeuralNetwork(len(text_features_train[0]), 120, len(emotion_set))\

        # train the neural network
        num_epochs = 2000
        lr = 0.001
        nn.train(X, y, val_targets, text_features_val, num_epochs=num_epochs, learning_rate=lr)

        scores_fold = nn.get_scores()
        scores.append(scores_fold)
        if scores_fold[-1] > best_score:
            best_nn = nn
            best_score = scores_fold[-1]
        logger.info(f"Best Accuracy = {best_score * 100:.2f}%")

    for score in scores:
        plt.plot(np.arange(len(score)), score)
    plt.title(f"NN: {folds}-fold Cross Validation, lr={lr}, epochs={num_epochs}, acc={best_score}")
    plt.xlabel("Iteration")
    plt.ylabel("Validation Accuracy")
    plt.savefig(f"NN_highestAcc={best_score}_{folds}-fold Cross Validation_lr={lr}_epochs={num_epochs}.png")

    pred_test = best_nn.predict(text_features_test)
    largest_idx = np.argmax(pred_test, axis=1)
    # logger.debug(largest_idx)
    test_pred = np.eye(pred_test.shape[1])[largest_idx]
    # logger.debug(np.argmax(val_pred))
    predicted_emotions = []
    for pred_emotion in np.argmax(test_pred, axis=1):      
        predicted_emotions.append(int2emotion[pred_emotion])

    test_set['emotions'] = predicted_emotions
    test_set.to_csv("./test_nn.csv")
    logger.info(f"Saving test results...")

if __name__ == '__main__':
    print ("..................Beginning of Logistic Regression................")
    # LR()
    print ("..................End of Logistic Regression................")

    print("------------------------------------------------")

    print ("..................Beginning of Neural Network................")
    NN()
    print ("..................End of Neural Network................")