from torch.utils.data import Dataset
import pandas as pd

# https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
class WiCDataset(Dataset):

    def __init__(self, file_path):
        # Read the csv files from certain file path
        self.data = pd.read_csv(file_path, sep='\t',\
                                header=None, lineterminator='\n',\
                                    names=["Target", "POS", "index1-2", "example1", "example2"])

    def __len__(self):
        return len(self.data)
    
    def __head__(self):
        return self.data.head()
    
    def __getitem__(self, idx):
        target = self.data.loc[idx, "Target"]
        
        # Part-of-Speech tag of the target word
        POS = self.data.loc[idx, "POS"] 
        
        # The index word in example 1 and example 2, respectively
        index1, index2 = self.data.loc[idx, "index1-2"].split("-")
        context1 = self.data.loc[idx, "example1"]
        context2 = self.data.loc[idx, "example2"]

        dic_data = {"target": target, "POS": POS, "index1": index1, \
                    "index2": index2, "context1": context1,\
                        "context2": context2}
        return dic_data