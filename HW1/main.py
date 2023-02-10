import pandas as pd
import numpy as np

from loguru import logger

def read_csv(path: str) -> pd.DataFrame:
    file = pd.read_csv(path)
    return file


def pre_processing(file: pd.DataFrame):
    return id, 

def LR():
    TRAIN_DATA = read_csv("./train.csv")
    # your logistic regression 
    pass


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