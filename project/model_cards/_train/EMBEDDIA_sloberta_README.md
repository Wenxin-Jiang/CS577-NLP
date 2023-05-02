---
language: 
- sl

license: cc-by-sa-4.0
---
# Usage
Load in transformers library with:
```
from transformers import AutoTokenizer, AutoModelForMaskedLM
  
  tokenizer = AutoTokenizer.from_pretrained("EMBEDDIA/sloberta")
  model = AutoModelForMaskedLM.from_pretrained("EMBEDDIA/sloberta")
```


# SloBERTa
SloBERTa model is a monolingual Slovene BERT-like model. It is closely related to French Camembert model https://camembert-model.fr/. The corpora used for training the model have 3.47 billion tokens in total. The subword vocabulary contains 32,000 tokens. The scripts and programs used for data preparation and training the model are available on https://github.com/clarinsi/Slovene-BERT-Tool

SloBERTa was trained for 200,000 iterations or about 98 epochs.

## Corpora
The following corpora were used for training the model:
* Gigafida 2.0
* Kas 1.0
* Janes 1.0 (only Janes-news, Janes-forum, Janes-blog, Janes-wiki subcorpora)
* Slovenian parliamentary corpus siParl 2.0
* slWaC

