---
language: fr
datasets:
- Jean-Baptiste/wikiner_fr
widget:
- text: "Je m'appelle jean-baptiste et je vis à montréal"
- text: "george washington est allé à washington"
license: mit
---

# camembert-ner: model fine-tuned from camemBERT for NER task.

## Introduction

[camembert-ner] is a NER model that was fine-tuned from camemBERT on wikiner-fr dataset.
Model was trained on wikiner-fr dataset (~170 634  sentences).
Model was validated on emails/chat data and overperformed other models on this type of data specifically. 
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


## How to use camembert-ner with HuggingFace

##### Load camembert-ner and its sub-word tokenizer :

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")


##### Process text sample (from wikipedia)

from transformers import pipeline

nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
nlp("Apple est créée le 1er avril 1976 dans le garage de la maison d'enfance de Steve Jobs à Los Altos en Californie par Steve Jobs, Steve Wozniak et Ronald Wayne14, puis constituée sous forme de société le 3 janvier 1977 à l'origine sous le nom d'Apple Computer, mais pour ses 30 ans et pour refléter la diversification de ses produits, le mot « computer » est retiré le 9 janvier 2015.")


[{'entity_group': 'ORG',
  'score': 0.9472818374633789,
  'word': 'Apple',
  'start': 0,
  'end': 5},
 {'entity_group': 'PER',
  'score': 0.9838564991950989,
  'word': 'Steve Jobs',
  'start': 74,
  'end': 85},
 {'entity_group': 'LOC',
  'score': 0.9831605950991312,
  'word': 'Los Altos',
  'start': 87,
  'end': 97},
 {'entity_group': 'LOC',
  'score': 0.9834540486335754,
  'word': 'Californie',
  'start': 100,
  'end': 111},
 {'entity_group': 'PER',
  'score': 0.9841555754343668,
  'word': 'Steve Jobs',
  'start': 115,
  'end': 126},
 {'entity_group': 'PER',
  'score': 0.9843501806259155,
  'word': 'Steve Wozniak',
  'start': 127,
  'end': 141},
 {'entity_group': 'PER',
  'score': 0.9841533899307251,
  'word': 'Ronald Wayne',
  'start': 144,
  'end': 157},
 {'entity_group': 'ORG',
  'score': 0.9468960364659628,
  'word': 'Apple Computer',
  'start': 243,
  'end': 257}]

```


## Model performances (metric: seqeval)

Overall

precision|recall|f1
-|-|-
0.8859|0.8971|0.8914

By entity

entity|precision|recall|f1
-|-|-|-
PER|0.9372|0.9598|0.9483 
ORG|0.8099|0.8265|0.8181
LOC|0.8905|0.9005|0.8955
MISC|0.8175|0.8117|0.8146




For those who could be interested, here is a short article on how I used the results of this model to train a LSTM model for signature detection in emails:
https://medium.com/@jean-baptiste.polle/lstm-model-for-email-signature-detection-8e990384fefa
