from torch.utils.data import Dataset
import pandas as pd

# https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
class WiCDataset(Dataset):

    def __init__(self, data_path, label_path):
        self.data_path = data_path
        self.label_path = label_path

        # Read the csv files from certain file path
        self.data = pd.read_csv(data_path, sep='\t',header=None,\
                                    names=["Target", "POS", "index1-2", "example1", "example2"])
        self.label = pd.read_csv(label_path, sep='\t', header=None,\
                                    names=["Label"])
    def __len__(self):
        if len(self.data) == len(self.label):
            return len(self.data)
        else:
            raise AssertionError(f"File sizes do not match each other: {self.data_path.split('/')[-1]}, {self.label_path.split('/')[-1]}")
    
    def __head__(self):
        return self.data.head()
    
    def __getitem__(self, idx):
        target = self.data.loc[idx, "Target"]
        POS = self.data.loc[idx, "POS"]
        index1, index2 = self.data.loc[idx, "index1-2"].split("-")
        context1 = self.data.loc[idx, "example1"]
        context2 = self.data.loc[idx, "example2"]

        label = self.label.loc[idx, "Label"]
        dic_data = {"label": label, "target": target, "POS": POS, "index1": index1, \
                    "index2": index2, "context1": context1,\
                        "context2": context2}
        return dic_data