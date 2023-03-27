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
from collections import defaultdict

import matplotlib.pyplot as plt #TODO: Command out in submission

from neural_archs import DAN, RNN, LSTM
from utils import WiCDataset, pad_embeddings, collate_fn, map_pos 

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    #  export KMP_DUPLICATE_LIB_OK=TRUE
    # TODO: change the `default' attribute in the following 3 lines with the choice
    # that achieved the best performance for your case
    parser.add_argument('--neural_arch', choices=['dan', 'rnn', 'lstm'], default='lstm', type=str)
    parser.add_argument('--rnn_bidirect', default=True, action='store_true')
    parser.add_argument('--init_word_embs', choices=['scratch', 'glove'], default='scratch', type=str)

    args = parser.parse_args()

    nltk.download("omw-1.4")
    nltk.download("wordnet")
    if args.init_word_embs == "glove":
        # TODO: Feed the GloVe embeddings to NN modules appropriately
        # for initializing the embeddings
        glove_embs = api.load("glove-wiki-gigaword-50")
        embedding_dim  = glove_embs.vector_size
        vocab_size = len(glove_embs)
        print(f"Glove Embedding size is {embedding_dim}")
        # unknown words just use zeros

        word_to_idx = {word: idx for idx, word in enumerate(glove_embs.index_to_key)}
        weights = torch.zeros((vocab_size, embedding_dim), dtype=torch.float32)
        embedding = torch.nn.Embedding.from_pretrained(weights, freeze=False)

    else:
        word_to_idx = defaultdict(lambda: len(word_to_idx))
        vocab_size = len(word_to_idx)
        lemma_embedding_dim = 300
        embedding_dim = 300
        embedding = torch.nn.Embedding(vocab_size, embedding_dim)
    
    
    lemma_embedding_dim = 50 if args.init_word_embs=="glove" else 300
    lemma_to_idx = defaultdict(lambda: len(lemma_to_idx))
    lemma_embedding = torch.nn.Embedding(len(lemma_to_idx), lemma_embedding_dim)
    
    input_size = embedding_dim
    hidden_size = 10
    output_size = 2

    # TODO: Freely modify the inputs to the declaration of each module below
    if args.neural_arch == "dan":
        model = DAN(input_size, hidden_size, output_size, dropout_rate=0.6).to(torch_device)
    elif args.neural_arch == "rnn":
        # if args.rnn_bidirect:
        model = RNN(input_size, hidden_size, output_size, num_layers=1, dropout_rate=0.6, bidirectional=args.rnn_bidirect).to(torch_device)
        # else:
        #     model = RNN().to(torch_device)
    elif args.neural_arch == "lstm":
        # if args.rnn_bidirect:
        model = LSTM(input_size, hidden_size, output_size, num_layers=1, dropout_rate=0.6, bidirectional=args.rnn_bidirect).to(torch_device)
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

    lemmatizer = WordNetLemmatizer()
    for dataset in [train_set, dev_set, test_set]:
        for i in range(len(dataset)):
            target = dataset[i]["target"]
            context1 = dataset[i]["context1"]
            context2 = dataset[i]["context2"]      
            
            pos = dataset[i]["POS"]
            wordnet_pos = map_pos(pos)
            lemma = lemmatizer.lemmatize(target, pos=wordnet_pos)

            tokens1 = context1.split()
            tokens2 = context2.split()
            indices1, indices2 =  [], []

            for word in tokens1:
                if word not in word_to_idx:
                    word_to_idx[word] = len(word_to_idx)
                    new_embedding = torch.rand(1, embedding_dim)
                    new_weights = torch.cat((embedding.weight.data, new_embedding))
                    embedding = torch.nn.Embedding.from_pretrained(new_weights, freeze=False)
                indices1.append(word_to_idx[word])
            
            for word in tokens2:
                if word not in word_to_idx:
                    word_to_idx[word] = len(word_to_idx)
                    new_embedding = torch.rand(1, embedding_dim)
                    new_weights = torch.cat((embedding.weight.data, new_embedding))
                    embedding = torch.nn.Embedding.from_pretrained(new_weights, freeze=False)
                indices2.append(word_to_idx[word])

            embeddings1 = embedding(torch.tensor(indices1)).unsqueeze(0)
            embeddings2 = embedding(torch.tensor(indices2)).unsqueeze(0)
            # print(embeddings1.shape, embeddings2.shape)
            # print(embeddings1, embeddings2)
            # pad shorter embedding to match each other.
            max_length = max(embeddings1.shape[1], embeddings2.shape[1])
            # print(max_length)
            embeddings1 = pad_embeddings(embeddings1, max_length)
            embeddings2 = pad_embeddings(embeddings2, max_length)

            if lemma not in lemma_to_idx:
                lemma_to_idx[lemma] = len(lemma_to_idx)
                new_embedding = torch.rand(1, lemma_embedding_dim)
                new_weights = torch.cat((lemma_embedding.weight.data, new_embedding))
                lemma_embedding = torch.nn.Embedding.from_pretrained(new_weights, freeze=False)
            
            lemma_idx = lemma_to_idx[lemma]
            # print("Embedding layer size:", lemma_embedding.weight.size())
            # print("Lemma_idx size:", lemma_idx)
            # print("Lemma_idx values:", lemma_idx)
            lemma_embedding_tensor = lemma_embedding(torch.tensor(lemma_idx)).unsqueeze(0).unsqueeze(1)
            # print(lemma_embedding)

            embeddings1 = torch.cat((embeddings1, lemma_embedding_tensor), dim=1)
            embeddings2 = torch.cat((embeddings2, lemma_embedding_tensor), dim=1)
            # input = (embeddings1, embeddings2) #TODO: Do I need to concat here?
            # print(embeddings1.shape, embeddings2.shape)
            input = torch.cat((embeddings1, embeddings2), dim=0)
            dataset.update(i, input)
            # print(input.shape)
        print(f"Sequences in {dataset} have been initialized!! Len({dataset}) is {len(dataset)}")

    train_dataloader = torch.utils.data.DataLoader(train_set, batch_size=32, shuffle=True, collate_fn=collate_fn)
    dev_dataloader = torch.utils.data.DataLoader(dev_set, batch_size=32, shuffle=True, collate_fn=collate_fn)
    test_dataloader = torch.utils.data.DataLoader(test_set, batch_size=32, shuffle=True, collate_fn=collate_fn)


    # TODO: Training and validation loop here
    num_epochs = 200
    lr = 1e-5
    log_test_curve = True

    train_losses = []
    train_accs = []
    val_losses = []
    val_accs = []

    if log_test_curve == True:
        test_losses = []
        test_accs = []

    criterion_train = torch.nn.CrossEntropyLoss()
    criterion_val = torch.nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-5)

    # TODO: Add lr scheduler and see how it works
    # # Add this after initializing the optimizer
    # scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', factor=0.5, patience=5)

    # # Update the learning rate scheduler in the training loop after the validation loss is calculated
    # scheduler.step(val_loss)


    print(f"Starting training on {torch_device}, hidden_size: {hidden_size}, num_epochs: {num_epochs}, lr: {lr}...")
    for epoch in range(num_epochs):
        model.train()
        train_loss = 0
        train_correct = 0
        
        for batch in train_dataloader:
            inputs, targets = batch
            optimizer.zero_grad()
            inputs = inputs.to(torch_device)
            targets = targets.to(torch_device)
            
            inputs = inputs.detach()
            outputs = model(inputs)
            
            # convert outputs to one-hot vectors
            # preds = torch.argmax(outputs, dim=1)
            # outputs.reshape(4, 2)
            # print(outputs.shape)
            loss_train = criterion_train(outputs, targets.long())
            # loss.backward(retain_graph=True)
            
            loss_train.backward()
            optimizer.step()

            train_loss += loss_train.item()
            preds = torch.argmax(outputs, dim=1)
            train_correct += (preds == targets).sum().item()
        
        train_loss /= len(train_dataloader)
        train_losses.append(train_loss)
        train_acc = train_correct / len(train_set)
        train_accs.append(train_acc)

        # Validation
        model.eval()
        val_loss = 0
        val_correct = 0

        with torch.no_grad():
            for batch in dev_dataloader: #TODO: check if dev==val
                inputs, targets = batch
                

                inputs = inputs.to(torch_device)
                targets = targets.to(torch_device)

                inputs = inputs.detach()

                outputs = model(inputs)
                # convert outputs to one-hot vectors
                # preds = torch.argmax(outputs, dim=1)
                loss_val = criterion_val(outputs, targets.long())

                val_loss += loss_val.item()
                preds = torch.argmax(outputs, dim=1)
                # print(preds.shape, targets.shape)
                val_correct += (preds == targets).sum().item()

        val_loss /= len(dev_dataloader)
        val_acc = val_correct / len(dev_set)
        val_losses.append(val_loss)
        val_accs.append(val_acc)

        if log_test_curve == True:
            # Test loop
            model.eval()
            test_loss = 0
            test_correct = 0

            with torch.no_grad():
                for batch in test_dataloader: #TODO: check if dev==val
                    inputs, targets = batch
                    

                    inputs = inputs.to(torch_device)
                    targets = targets.to(torch_device)

                    inputs = inputs.detach()

                    outputs = model(inputs)
                    # convert outputs to one-hot vectors
                    # preds = torch.argmax(outputs, dim=1)
                    loss_test = criterion_val(outputs, targets.long())

                    test_loss += loss_test.item()
                    preds = torch.argmax(outputs, dim=1)
                    # print(preds.shape, targets.shape)
                    test_correct += (preds == targets).sum().item()

            test_loss /= len(test_dataloader)
            test_acc = test_correct / len(test_set)
            test_losses.append(test_loss)
            test_accs.append(test_acc)
        print(f"Epoch {epoch+1}/{num_epochs}, Train loss: {train_loss:.4f}, Train accuracy: {train_acc:.4f}, Val loss: {val_loss:.4f}, Val acc: {val_acc:.4f}")
    
    
    
    # TODO: Testing loop
    # Write predictions (F or T) for each test example into test.pred.txt
    # One line per each example, in the same order as test.data.txt.
    model. eval()
    test_correct = 0
    with open("test.pred.txt", "w") as pred_file:
        for batch in test_dataloader:
            inputs, targets = batch
            
            inputs = inputs.to(torch_device)
            targets = targets.to(torch_device)
        
            outputs = model(inputs)
            preds = torch.argmax(outputs, dim=1)
            test_correct += (preds == targets).sum().item()
            preds = ["T" if pred.item() == 1 else "F" for pred in preds]
            for pred in preds:
                pred_file.write(f"{pred}\n")
        test_acc = test_correct / len(test_set)
        print(f"Test acc: {test_acc:.4f}")
    
    fileName_bi = "_bi" if args.rnn_bidirect else None
    plt.plot(np.arange(len(train_losses)), train_losses, label="Train")
    plt.plot(np.arange(len(val_losses)), val_losses, label="Val")
    if log_test_curve == True:
        plt.plot(np.arange(len(test_losses)), test_losses, label="Test")
    plt.title(f"{args.neural_arch}_{args.init_word_embs}: hidden{hidden_size}, epoch={num_epochs}, lr={lr}, test_acc={test_acc*100:.2f}%")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig(f"{args.neural_arch}_{args.init_word_embs}_Loss{fileName_bi}_hidden{hidden_size}_epoch{num_epochs}_lr{lr}_testAcc{test_acc*100:.2f}.jpg")
    plt.close()

    plt.plot(np.arange(len(train_accs)), train_accs, label="Train")
    plt.plot(np.arange(len(val_accs)), val_accs, label="Val")
    if log_test_curve == True:
        plt.plot(np.arange(len(test_accs)), test_accs, label="Test")
    plt.title(f"{args.neural_arch}_{args.init_word_embs}: hidden{hidden_size}, epoch={num_epochs}, lr={lr}, test_acc={test_acc*100:.2f}%")
    plt.xlabel("Iterations")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.savefig(f"{args.neural_arch}_{args.init_word_embs}_Acc{fileName_bi}_hidden{hidden_size}_epoch{num_epochs}_lr{lr}_testAcc{test_acc*100:.2f}%.jpg")
    plt.close()