---
language: en
datasets:
- conll2003
widget:
- text: "My name is jean-baptiste and I live in montreal"
- text: "My name is clara and I live in berkeley, california."
- text: "My name is wolfgang and I live in berlin"
train-eval-index:
- config: conll2003
  task: token-classification
  task_id: entity_extraction
  splits:
    eval_split: validation
  col_mapping:
    tokens: tokens
    ner_tags: tags
license: mit

---

# roberta-large-ner-english: model fine-tuned from roberta-large for NER task

## Introduction

[roberta-large-ner-english] is an english NER model that was fine-tuned from roberta-large on conll2003 dataset. 
Model was validated on emails/chat data and outperformed other models on this type of data specifically. 
In particular the model seems to work better on entity that don't start with an upper case.


## Training data

Training data was classified as follow:

Abbreviation|Description
-|-
O |Outside of a named entity
MISC |Miscellaneous entity
PER |Person’s name
ORG |Organization
LOC |Location

In order to simplify, the prefix B- or I- from original conll2003 was removed.
I used the train and test dataset from original conll2003 for training and the "validation" dataset for validation. This resulted in a dataset of size:

Train | Validation 
-|-
17494 | 3250

## How to use roberta-large-ner-english with HuggingFace

##### Load roberta-large-ner-english and its sub-word tokenizer :

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-large-ner-english")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-large-ner-english")


##### Process text sample (from wikipedia)

from transformers import pipeline

nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
nlp("Apple was founded in 1976 by Steve Jobs, Steve Wozniak and Ronald Wayne to develop and sell Wozniak's Apple I personal computer")


[{'entity_group': 'ORG',
  'score': 0.99381506,
  'word': ' Apple',
  'start': 0,
  'end': 5},
 {'entity_group': 'PER',
  'score': 0.99970853,
  'word': ' Steve Jobs',
  'start': 29,
  'end': 39},
 {'entity_group': 'PER',
  'score': 0.99981767,
  'word': ' Steve Wozniak',
  'start': 41,
  'end': 54},
 {'entity_group': 'PER',
  'score': 0.99956465,
  'word': ' Ronald Wayne',
  'start': 59,
  'end': 71},
 {'entity_group': 'PER',
  'score': 0.9997918,
  'word': ' Wozniak',
  'start': 92,
  'end': 99},
 {'entity_group': 'MISC',
  'score': 0.99956393,
  'word': ' Apple I',
  'start': 102,
  'end': 109}]
```


## Model performances 

Model performances computed on conll2003 validation dataset (computed on the tokens predictions)

entity|precision|recall|f1
-|-|-|-
PER|0.9914|0.9927|0.9920 
ORG|0.9627|0.9661|0.9644
LOC|0.9795|0.9862|0.9828
MISC|0.9292|0.9262|0.9277
Overall|0.9740|0.9766|0.9753


On private dataset (email, chat, informal discussion), computed on word predictions:

entity|precision|recall|f1
-|-|-|-
PER|0.8823|0.9116|0.8967
ORG|0.7694|0.7292|0.7487
LOC|0.8619|0.7768|0.8171

By comparison on the same private dataset, Spacy (en_core_web_trf-3.2.0) was giving:

entity|precision|recall|f1
-|-|-|-
PER|0.9146|0.8287|0.8695
ORG|0.7655|0.6437|0.6993
LOC|0.8727|0.6180|0.7236



For those who could be interested, here is a short article on how I used the results of this model to train a LSTM model for signature detection in emails:
https://medium.com/@jean-baptiste.polle/lstm-model-for-email-signature-detection-8e990384fefa
