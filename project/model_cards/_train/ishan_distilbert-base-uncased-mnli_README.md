---
language: en
thumbnail: 
tags:
- pytorch
- text-classification
datasets:
- MNLI
---

# distilbert-base-uncased finetuned on MNLI

## Model Details and Training Data

We used the pretrained model from [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) and finetuned it on [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/) dataset. 

The training parameters were kept the same as [Devlin et al., 2019](https://arxiv.org/abs/1810.04805) (learning rate = 2e-5, training epochs = 3, max_sequence_len = 128 and batch_size = 32).

## Evaluation Results

The evaluation results are mentioned in the table below.

| Test Corpus | Accuracy |
|:---:|:---------:|
| Matched | 0.8223 |
| Mismatched | 0.8216 |

