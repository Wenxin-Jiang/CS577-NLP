---
language:
- fr
tags:
- classification
license: apache-2.0
metrics:
- accuracy
widget:
- text: "tchai on est morts. on va se faire vacciner et ils vont contrôler comme les marionnettes avec des fils. d'après les 'ont dit'..."
---
# camembert-fr-covid-tweet-sentiment-classification
This model is a fine-tune checkpoint of [Yanzhu/bertweetfr-base](https://huggingface.co/Yanzhu/bertweetfr-base), fine-tuned on SST-2.
This model reaches an accuracy of 71% on the dev set.
In this dataset, given a tweet, the goal was to infer the underlying topic of the tweet by choosing from four topics classes:
- 0 : negatif
- 1 : neutre 
- 2 : positif


# Pipelining the Model
 
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
tokenizer = AutoTokenizer.from_pretrained("Monsia/camembert-fr-covid-tweet-sentiment-classification")
model = AutoModelForSequenceClassification.from_pretrained("Monsia/camembert-fr-covid-tweet-sentiment-classification")
nlp_topic_classif = transformers.pipeline('topics-classification', model = model, tokenizer = tokenizer)
nlp_topic_classif("tchai on est morts. on va se faire vacciner et ils vont contrôler comme les marionnettes avec des fils. d'après les '' ont dit ''...")
# Output: [{'label': 'opinions', 'score': 0.831]
```