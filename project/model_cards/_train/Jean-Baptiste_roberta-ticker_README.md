---
language: en
widget:
- text: "I am going to buy 100 shares of cake tomorrow"
---

# roberta-ticker: model was fine-tuned from Roberta to detect financial tickers

## Introduction

This is a model specifically designed to identify tickers in text.
Model was trained on transformed dataset from following Kaggle dataset:
https://www.kaggle.com/omermetinn/tweets-about-the-top-companies-from-2015-to-2020



## How to use roberta-ticker with HuggingFace

##### Load roberta-ticker and its sub-word tokenizer :

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-ticker")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-ticker")


##### Process text sample 

from transformers import pipeline

nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

nlp("I am going to buy 100 shares of cake tomorrow")
[{'entity_group': 'TICKER',
  'score': 0.9612462520599365,
  'word': ' cake',
  'start': 32,
  'end': 36}]
  
nlp("I am going to eat a cake tomorrow")
[]
 


```


## Model performances


```
precision: 0.914157
recall: 0.788824
f1: 0.846878

 ```

