---
language:
- en
tags:
- text Classification
license: apache-2.0
widget:
- text: "I like you. </s></s> I love you."

---

* IMDBSentimentDistilBertModel:

- I have used IMDB movie review dataset to create custom model by using DistilBertForSequenceClassification.

from transformers import DistilBertForSequenceClassification, Trainer, TrainingArguments

model = DistilBertForSequenceClassification.from_pretrained('./imdbsentdistilbertmodel')


