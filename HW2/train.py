import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import argparse
import random
random.seed(577)

import numpy as np
np.random.seed(577)

import torch
torch.set_default_tensor_type(torch.FloatTensor)
torch.use_deterministic_algorithms(True)
torch.manual_seed(577)
torch_device = torch.device("cpu")

'''
NOTE: Do not change any of the statements above regarding random/numpy/pytorch.
You can import other built-in libraries (e.g. collections) or pre-specified external libraries
such as pandas, nltk and gensim below. 
Also, if you'd like to declare some helper functions, please do so in utils.py and
change the last import statement below.
'''

import gensim.downloader as api

from neural_archs import DAN, RNN, LSTM
from utils import WiCDataset


def words_to_embeddings(words, embedding_size, init_word_embs="scratch", glove_model=None):
    word_embeddings = []
    if init_word_embs == "glove":
        glove_model = api.load("glove-wiki-gigaword-50")
        for word in words:
            if word in glove_model.index_to_key:
                word_embeddings.append(glove_model[word])
            else:
                print(f"{word} does not exist in glove_model!!! Appending zeros as input.")
                word_embeddings.append(np.zeros(embedding_size)) # TODO: test if necessary
        return np.stack(word_embeddings)
    elif init_word_embs == "scratch":
        # TODO
        pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # TODO: change the `default' attribute in the following 3 lines with the choice
    # that achieved the best performance for your case
    parser.add_argument('--neural_arch', choices=['dan', 'rnn', 'lstm'], default='dan', type=str)
    parser.add_argument('--rnn_bidirect', default=False, action='store_true')
    parser.add_argument('--init_word_embs', choices=['scratch', 'glove'], default='scratch', type=str)

    args = parser.parse_args()

    if args.init_word_embs == "glove":
        # TODO: Feed the GloVe embeddings to NN modules appropriately
        # for initializing the embeddings
        glove_embs = api.load("glove-wiki-gigaword-50")
        embedding_size = glove_embs.vector_size
        print(f"Glove Embedding size is {embedding_size}")

    input_size = embedding_size
    hidden_size = 128
    output_size = 2

    # TODO: Freely modify the inputs to the declaration of each module below
    if args.neural_arch == "dan":
        model = DAN(input_size, hidden_size, output_size).to(torch_device)
    elif args.neural_arch == "rnn":
        # if args.rnn_bidirect:
        model = RNN(input_size, hidden_size, output_size, num_layers=1, bidirectional=args.rnn_bidirect).to(torch_device)
        # else:
        #     model = RNN().to(torch_device)
    elif args.neural_arch == "lstm":
        # if args.rnn_bidirect:
        model = LSTM(input_size, hidden_size, output_size, num_layers=1, bidirectional=args.rnn_bidirect).to(torch_device)
        # else:
        #     model = LSTM().to(torch_device)

    # TODO: Read off the WiC dataset files from the `WiC_dataset' directory
    # (will be located in /homes/cs577/WiC_dataset/(train, dev, test))
    # and initialize PyTorch dataloader appropriately
    # Take a look at this page
    # https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
    # and implement a PyTorch Dataset class for the WiC dataset in
    # utils.py
    train_data_path = "./WiC_dataset/train/train.data.txt"
    dev_data_path = "./WiC_dataset/dev/dev.data.txt"
    test_data_path = "./WiC_dataset/test/test.data.txt"
    
    train_label_path = "./WiC_dataset/train/train.gold.txt"
    dev_label_path = "./WiC_dataset/dev/dev.gold.txt"
    test_label_path = "./WiC_dataset/test/test.gold.txt"

    train_set = WiCDataset(train_data_path, train_label_path)
    dev_set = WiCDataset(dev_data_path, dev_label_path)
    test_set = WiCDataset(test_data_path, test_label_path)

    for dataset in [train_set, dev_set, test_set]:
        for i in range(len(dataset)):
            target = dataset[i]["target"]
            context1 = dataset[i]["context1"]
            context2 = dataset[i]["context2"]      
            input = context1.split() + context2.split()
            dataset[i]["input"] = words_to_embeddings(input, embedding_size, \
                                                      init_word_embs=args.init_word_embs)
    
    train_dataloader = torch.utils.data.DataLoader(train_set, batch_size=32, shuffle=True)
    dev_dataloader = torch.utils.data.DataLoader(dev_set, batch_size=32, shuffle=True)
    test_dataloader = torch.utils.data.DataLoader(test_set, batch_size=32, shuffle=True)


    # TODO: Training and validation loop here
    num_epochs = 10
    lr = 0.001

    loss_CE = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(num_epochs):
        model.train()
        train_loss = 0
        train_correct = 0

        for batch in train_dataloader:
            inputs = batch["input"].to(torch_device)
            targets = batch["target"].to(torch_device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = loss_CE(outputs, targets)

            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            preds = torch.argmax(outputs, dim=1)
            train_correct += (preds == targets).sum().item()
        
        train_loss /= len(train_dataloader)
        train_acc = train_correct / len(train_set)

        # Validation
        model.eval()
        val_loss = 0
        val_correct = 0

        with torch.no_grad():
            for batch in dev_dataloader: #TODO: check if dev==val
                inputs = batch["input"].to(torch_device)
                targets = batch["target"].to(torch_device)

                outputs = model(inputs)
                loss = loss_CE(outputs, targets)

                val_loss += loss.item()
                preds = torch.argmax(outputs, dim=1)
                val_correct += (preds == targets).sum().item()

        val_loss /= len(dev_dataloader)
        val_acc = val_correct / len(dev_dataloader)

        print(f"Epoch {epoch+1}/{num_epochs}, Train loss: {train_loss:.4f},\
               Train accuracy: {train_acc:.4f},\nVal loss: {val_loss:.4f}, Val acc: {val_acc:.4f}")
    # TODO: Testing loop
    # Write predictions (F or T) for each test example into test.pred.txt
    # One line per each example, in the same order as test.data.txt.
    model. eval()
    with open("test.pred.txt", "w") as pred_file:
        for batch in test_dataloader:
            inputs = batch["input"].to(torch_device)
            outputs = model(inputs)
            preds = torch.argmax(outputs, dim=1)
            preds = ["T" if pred.item() == 1 else "F" for pred in preds]
            for pred in preds:
                pred_file.write(f"{pred}\n")