## Classifier to check if two sequences are paraphrase or not

Trained based on ruBert by DeepPavlov.

Use this way:
```
import torch
import torch.nn as nn
import os
import copy
import random
import numpy as np
import pandas as pd
from torch.utils.data import DataLoader, Dataset
from torch.cuda.amp import autocast, GradScaler
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel, AdamW, get_linear_schedule_with_warmup

from transformers.file_utils import (
    cached_path,
    hf_bucket_url,
    is_remote_url,
)

archive_file = hf_bucket_url(
                "alenusch/par_cls_bert",
                filename="rubert-base-cased_lr_2e-05_val_loss_0.66143_ep_4.pt",
                revision=None,
                mirror=None,
            )
resolved_archive_file = cached_path(
                archive_file,
                cache_dir=None,
                force_download=False,
                proxies=None,
                resume_download=False,
                local_files_only=False,
            )

os.environ["TOKENIZERS_PARALLELISM"] = "false"

class SentencePairClassifier(nn.Module):

    def __init__(self, bert_model):
        super(SentencePairClassifier, self).__init__()
        self.bert_layer = AutoModel.from_pretrained(bert_model)
        self.cls_layer = nn.Linear(768, 1)
        self.dropout = nn.Dropout(p=0.1)

    @autocast()
    def forward(self, input_ids, attn_masks, token_type_ids):
        cont_reps, pooler_output = self.bert_layer(input_ids, attn_masks, token_type_ids,  return_dict=False)
        logits = self.cls_layer(self.dropout(pooler_output))
        return logits

class CustomDataset(Dataset):

    def __init__(self, data, maxlen, bert_model):

        self.data = data
        self.tokenizer = AutoTokenizer.from_pretrained(bert_model)
        self.maxlen = maxlen
        self.targets = False

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        sent1 = str(self.data[index][0])
        sent2 = str(self.data[index][1])
        encoded_pair = self.tokenizer(sent1, sent2, 
                                      padding='max_length',  # Pad to max_length
                                      truncation=True,  # Truncate to max_length
                                      max_length=self.maxlen,  
                                      return_tensors='pt')  # Return torch.Tensor objects
        
        token_ids = encoded_pair['input_ids'].squeeze(0)  # tensor of token ids
        attn_masks = encoded_pair['attention_mask'].squeeze(0)  # binary tensor with "0" for padded values and "1" for the other values
        token_type_ids = encoded_pair['token_type_ids'].squeeze(0)  # binary tensor with "0" for the 1st sentence tokens & "1" for the 2nd sentence tokens

        return token_ids, attn_masks, token_type_ids

def get_probs_from_logits(logits):
    probs = torch.sigmoid(logits.unsqueeze(-1))
    return probs.detach().cpu().numpy()

def test_prediction(net, device, dataloader, with_labels=False):
    net.eval()
    probs_all = []

    with torch.no_grad():
        for seq, attn_masks, token_type_ids in tqdm(dataloader):
                seq, attn_masks, token_type_ids = seq.to(device), attn_masks.to(device), token_type_ids.to(device)
                logits = net(seq, attn_masks, token_type_ids)
                probs = get_probs_from_logits(logits.squeeze(-1)).squeeze(-1)
                probs_all += probs.tolist()
    return probs_all

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
cls_model = SentencePairClassifier(bert_model="alenusch/par_cls_bert")
if torch.cuda.device_count() > 1:
    cls_model = nn.DataParallel(model)

cls_model.load_state_dict(torch.load(resolved_archive_file))
cls_model.to(device)

variants = [["sentence1", "sentence2"]]
test_set = CustomDataset(variants, maxlen=512, bert_model="alenusch/par_cls_bert")
test_loader = DataLoader(test_set, batch_size=16, num_workers=5)
res = test_prediction(net=cls_model, device=device, dataloader=test_loader, with_labels=False)

```