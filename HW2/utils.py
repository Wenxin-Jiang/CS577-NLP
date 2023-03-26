from torch.utils.data import Dataset
import pandas as pd


import torch.nn.functional as F
from torch.nn.utils.rnn import pad_sequence
from nltk.corpus import wordnet
# https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
class WiCDataset(Dataset):

    def __init__(self, data_path, label_path, pos_mapper=None):
        self.data_path = data_path
        self.label_path = label_path

        # Read the csv files from certain file path
        self.data = pd.read_csv(data_path, sep='\t',header=None,\
                                    names=["Target", "POS", "index1-2", "example1", "example2"])
        self.label = pd.read_csv(label_path, sep='\t', header=None,\
                                    names=["Label"])
        self.inputs = [None] * len(self.data)

        if pos_mapper is not None:
            self.data['POS']= self.data['POS'].apply(pos_mapper)

        
    def __len__(self):
        if len(self.data) == len(self.label):
            return len(self.data)
        else:
            raise AssertionError(f"File sizes do not match each other: {self.data_path.split('/')[-1]}, {self.label_path.split('/')[-1]}")
    
    def __head__(self):
        return self.data.head()
    
    def __getitem__(self, idx):
        input_value = self.inputs[idx]

        target = self.data.loc[idx, "Target"]
        POS = self.data.loc[idx, "POS"]
        index1, index2 = self.data.loc[idx, "index1-2"].split("-")
        context1 = self.data.loc[idx, "example1"]
        context2 = self.data.loc[idx, "example2"]

        label = self.label.loc[idx, "Label"]
        dic_data = {"label": label, "target": target, "POS": POS, "index1": index1, \
                "index2": index2, "context1": context1,\
                    "context2": context2, "input": input_value}
        return dic_data
    
    def update(self, idx, input_value):
        self.inputs[idx] = input_value
        return


def map_pos(pos):
    if pos == "N":
        return wordnet.NOUN
    elif pos == "V":
        return wordnet.VERB
    else:
        return None

def pad_embeddings(tensor, max_length):
    pad_size = max_length - tensor.shape[1]
    padded_embeddings = F.pad(tensor, (0, 0, 0, pad_size, 0, 0))
    return padded_embeddings


def collate_fn(batch):
    inputs = [item["input"] for item in batch]
    labels = [item["label"] for item in batch]
    # print(inputs[0].shape)

    max_len1 = max([input[0].size(0) for input in inputs])
    max_len2 = max([input[1].size(0) for input in inputs])

    embeddings1_padded = [torch.cat([input[0], torch.zeros(max_len1 - input[0].size(0), input[0].size(1))], dim=0) for input in inputs]
    embeddings2_padded = [torch.cat([input[1], torch.zeros(max_len2 - input[1].size(0), input[1].size(1))], dim=0) for input in inputs]

    inputs_concat = [torch.cat([emb1, emb2], dim=0) for emb1, emb2 in zip(embeddings1_padded, embeddings2_padded)]

    padded_inputs = pad_sequence(inputs_concat, batch_first=True)
    for idx, label in enumerate(labels):
        if label == "F":
            labels[idx] = 0
        elif label == "T":
            labels[idx] = 1

    labels_tensor = torch.tensor(labels, dtype=torch.float32)

    return padded_inputs, labels_tensor


def words_to_embeddings(words, embedding_size, embedding_dim=50, init_word_embs="scratch", glove_model=None):
    word_embeddings = []
    vocab_size = embedding_size

    if init_word_embs == "scratch":
        embeddings = torch.nn.Embedding(vocab_size, embedding_size)
    elif init_word_embs == "glove":
        glove_model = api.load("glove-wiki-gigaword-50")
        weights = torch.zeros((vocab_size, embedding_size))
        for word in words:
            weights[i] = torch.tensor(glove_model[word], dtype=torch.float32)
        embeddings = torch.nn.Embedding.from_pretrained(weights, freeze=False)
    else:
        raise ValueError(f"{init_word_embs} is an invalid embedding method!")
    return embeddings
    # if init_word_embs == "glove":
    #     glove_model = api.load("glove-wiki-gigaword-50")
    #     for word in words:
    #         if word in glove_model.index_to_key:
    #             print(f"{word} exists in glove_model!!!.")
    #             word_embeddings.append(glove_model[word])
    #         else:
    #             print(f"{word} does not exist in glove_model!!! Appending zeros as input.")
    #             word_embeddings.append(np.zeros(embedding_size)) # TODO: test if necessary
    #     return np.stack(word_embeddings)
    # elif init_word_embs == "scratch":
        # TODO
