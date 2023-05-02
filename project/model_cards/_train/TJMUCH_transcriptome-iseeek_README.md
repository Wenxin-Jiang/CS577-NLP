
# iSEEEK
A universal approach for integrating super large-scale single-cell transcriptomes by exploring gene rankings

## An simple pipeline for single-cell analysis
```python
import torch
import gzip
import re
from tqdm import tqdm
import numpy as np
import scanpy as sc
from torch.utils.data import DataLoader, Dataset
from transformers import PreTrainedTokenizerFast, BertForMaskedLM 

class LineDataset(Dataset):
    def __init__(self, lines):
        self.lines = lines
        self.regex = re.compile(r'\-|\.')
    def __getitem__(self, i):
        return self.regex.sub('_', self.lines[i])
    def __len__(self):
        return len(self.lines)

device = "cuda" if torch.cuda.is_available() else "cpu" 
torch.set_num_threads(2)

tokenizer = PreTrainedTokenizerFast.from_pretrained("TJMUCH/transcriptome-iseeek")
model = BertForMaskedLM.from_pretrained("TJMUCH/transcriptome-iseeek").bert
model = model.to(device)
model.eval()


## Data desposited in https://huggingface.co/TJMUCH/transcriptome-iseeek/tree/main
lines = [s.strip().decode() for s in gzip.open("pbmc_ranking.txt.gz")]
labels = [s.strip().decode() for s in gzip.open("pbmc_label.txt.gz")]
labels = np.asarray(labels)


ds = LineDataset(lines)
dl = DataLoader(ds, batch_size=80)

features = []

for a in tqdm(dl, total=len(dl)):
    batch = tokenizer(a, max_length=128, truncation=True, 
               padding=True, return_tensors="pt")

    for k, v in batch.items():
        batch[k] = v.to(device)

    with torch.no_grad():
        out = model(**batch)

    f = out.last_hidden_state[:,0,:]
    features.extend(f.tolist())

features = np.stack(features)

adata = sc.AnnData(features)
adata.obs['celltype'] = labels
adata.obs.celltype = adata.obs.celltype.astype("category")
sc.pp.neighbors(adata, use_rep='X')
sc.tl.umap(adata)
sc.tl.leiden(adata)
sc.pl.umap(adata, color=['celltype','leiden'],save= "UMAP")

```

## Extract token representations 
```python

cell_counts = len(lines)
x = np.zeros((cell_counts, len(tokenizer)), dtype=np.float16)

for a in tqdm(dl, total=len(dl)):
    batch = tokenizer(a, max_length=128, truncation=True,
               padding=True, return_tensors="pt")

    for k, v in batch.items():
        batch[k] = v.to(device)

    with torch.no_grad():
        out = model(**batch)

    eos_idxs = batch.attention_mask.sum(dim=1) - 1
    f = out.last_hidden_state
    batch_size = f.shape[0]
    input_ids = batch.input_ids

    for i in range(batch_size):
        ##genes = tokenizer.batch_decode(input_ids[i])
        token_norms = [f[i][j].norm().item() for j in range(1, eos_idxs[i])]
        idxs = input_ids[i].tolist()[1:eos_idxs[i]]
        x[counter, idxs] = token_norms
        counter = counter + 1
```
