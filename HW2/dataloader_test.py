import torch

import utils
from utils import WiCDataset

from loguru import logger

train_set = WiCDataset("./WiC_dataset/train/train.data.txt")
print(train_set.__len__())