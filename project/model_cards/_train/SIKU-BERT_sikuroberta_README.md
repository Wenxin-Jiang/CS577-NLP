---
language: 
- "zh"
thumbnail: "https://raw.githubusercontent.com/SIKU-BERT/SikuBERT/main/appendix/sikubert.png"
tags:
- "chinese"
- "classical chinese"
- "literary chinese"
- "ancient chinese"
- "bert"
- "roberta"
- "pytorch"
inference: false 
license: "apache-2.0"
---
# SikuBERT
## Model description
![SikuBERT](https://raw.githubusercontent.com/SIKU-BERT/SikuBERT-for-digital-humanities-and-classical-Chinese-information-processing/main/appendix/sikubert.png)
Digital humanities research needs the support of large-scale corpus and high-performance ancient Chinese natural language processing tools. The pre-training language model has greatly improved the accuracy of text mining in English and modern Chinese texts. At present, there is an urgent need for a pre-training model specifically for the automatic processing of ancient texts. We used the verified high-quality “Siku Quanshu” full-text corpus as the training set, based on the BERT deep language model architecture, we constructed the SikuBERT and SikuRoBERTa pre-training language models for intelligent processing tasks of ancient Chinese. 
## How to use
```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("SIKU-BERT/sikuroberta")
model = AutoModel.from_pretrained("SIKU-BERT/sikuroberta")
```
## About Us
We are from Nanjing Agricultural University.
> Created with by SIKU-BERT [![Github icon](https://cdn0.iconfinder.com/data/icons/octicons/1024/mark-github-32.png)](https://github.com/SIKU-BERT/SikuBERT-for-digital-humanities-and-classical-Chinese-information-processing) 
