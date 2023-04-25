---
language: fr
datasets:
- Jean-Baptiste/wikiner_fr
widget:
- text: "Je m'appelle jean-baptiste et j'habite à montréal depuis fevr 2012"
---

# camembert-ner: model fine-tuned from camemBERT for NER task (including DATE tag).

## Introduction

[camembert-ner-with-dates] is an extension of french camembert-ner model with an additionnal tag for dates.
Model was trained on enriched version of wikiner-fr dataset (~170 634  sentences).

On my test data (mix of chat and email), this model got an f1 score of ~83% (in comparison dateparser was ~70%).
Dateparser library can still be be used on the output of this model in order to convert text to python datetime object 
(https://dateparser.readthedocs.io/en/latest/).


## How to use camembert-ner-with-dates with HuggingFace

##### Load camembert-ner-with-dates and its sub-word tokenizer :

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")


##### Process text sample (from wikipedia)

from transformers import pipeline

nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
nlp("Apple est créée le 1er avril 1976 dans le garage de la maison d'enfance de Steve Jobs à Los Altos en Californie par Steve Jobs, Steve Wozniak et Ronald Wayne14, puis constituée sous forme de société le 3 janvier 1977 à l'origine sous le nom d'Apple Computer, mais pour ses 30 ans et pour refléter la diversification de ses produits, le mot « computer » est retiré le 9 janvier 2015.")


[{'entity_group': 'ORG',
  'score': 0.9776379466056824,
  'word': 'Apple',
  'start': 0,
  'end': 5},
 {'entity_group': 'DATE',
  'score': 0.9793774570737567,
  'word': 'le 1er avril 1976 dans le',
  'start': 15,
  'end': 41},
 {'entity_group': 'PER',
  'score': 0.9958226680755615,
  'word': 'Steve Jobs',
  'start': 74,
  'end': 85},
 {'entity_group': 'LOC',
  'score': 0.995087186495463,
  'word': 'Los Altos',
  'start': 87,
  'end': 97},
 {'entity_group': 'LOC',
  'score': 0.9953305125236511,
  'word': 'Californie',
  'start': 100,
  'end': 111},
 {'entity_group': 'PER',
  'score': 0.9961076378822327,
  'word': 'Steve Jobs',
  'start': 115,
  'end': 126},
 {'entity_group': 'PER',
  'score': 0.9960325956344604,
  'word': 'Steve Wozniak',
  'start': 127,
  'end': 141},
 {'entity_group': 'PER',
  'score': 0.9957776467005411,
  'word': 'Ronald Wayne',
  'start': 144,
  'end': 157},
 {'entity_group': 'DATE',
  'score': 0.994030773639679,
  'word': 'le 3 janvier 1977 à',
  'start': 198,
  'end': 218},
 {'entity_group': 'ORG',
  'score': 0.9720810294151306,
  'word': "d'Apple Computer",
  'start': 240,
  'end': 257},
 {'entity_group': 'DATE',
  'score': 0.9924157659212748,
  'word': '30 ans et',
  'start': 272,
  'end': 282},
 {'entity_group': 'DATE',
  'score': 0.9934852868318558,
  'word': 'le 9 janvier 2015.',
  'start': 363,
  'end': 382}]

```


## Model performances (metric: seqeval)

Global
```
'precision': 0.928
'recall': 0.928
'f1': 0.928
```

By entity
```
Label LOC: (precision:0.929, recall:0.932, f1:0.931, support:9510)
Label PER: (precision:0.952, recall:0.965, f1:0.959, support:9399)
Label MISC: (precision:0.878, recall:0.844, f1:0.860, support:5364)
Label ORG: (precision:0.848, recall:0.883, f1:0.865, support:2299)
Label DATE: Not relevant because of method used to add date tag on wikiner dataset (estimated f1 ~90%)


 ```

