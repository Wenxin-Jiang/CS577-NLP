---
language:
- he 
tags:
- language model
license: apache-2.0
datasets:
- oscar
- wikipedia
- twitter 
---

# AlephBERT

## Hebrew Language Model

State-of-the-art language model for Hebrew.
Based on Google's BERT architecture [(Devlin et al. 2018)](https://arxiv.org/abs/1810.04805).

#### How to use

```python
from transformers import BertModel, BertTokenizerFast

alephbert_tokenizer = BertTokenizerFast.from_pretrained('onlplab/alephbert-base')
alephbert = BertModel.from_pretrained('onlplab/alephbert-base')

# if not finetuning - disable dropout
alephbert.eval()
```

## Training data
1. OSCAR [(Ortiz, 2019)](https://oscar-corpus.com/) Hebrew section (10 GB text, 20 million sentences).
2. Hebrew dump of [Wikipedia](https://dumps.wikimedia.org/hewiki/latest/) (650 MB text, 3 million sentences).
3. Hebrew Tweets collected from the Twitter sample stream (7 GB text, 70 million sentences).

## Training procedure

Trained on a DGX machine (8 V100 GPUs) using the standard huggingface training procedure.

Since the larger part of our training data is based on tweets we decided to start by optimizing using Masked Language Model loss only.

To optimize training time we split the data into 4 sections based on max number of tokens:

1. num tokens < 32 (70M sentences)
2. 32 <= num tokens < 64 (12M sentences)
3. 64 <= num tokens < 128 (10M sentences)
4. 128 <= num tokens < 512 (1.5M sentences)

Each section was first trained for 5 epochs with an initial learning rate set to 1e-4. Then each section was trained for another 5 epochs with an initial learning rate set to 1e-5, for a total of 10 epochs.

Total training time was 8 days.


