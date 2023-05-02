---
language:
- ru
tags:
- sentiment
- text-classification
datasets:
- Tatyana/ru_sentiment_dataset
---

# Keras model with ruBERT conversational embedder for Sentiment Analysis
Russian texts sentiment classification.

Model trained on [Tatyana/ru_sentiment_dataset](https://huggingface.co/datasets/Tatyana/ru_sentiment_dataset)

## Labels meaning
    0: NEUTRAL
    1: POSITIVE
    2: NEGATIVE

## How to use
```python

!pip install tensorflow-gpu
!pip install deeppavlov
!python -m deeppavlov install squad_bert
!pip install fasttext
!pip install transformers
!python -m deeppavlov install bert_sentence_embedder

from deeppavlov import build_model

model = build_model(Tatyana/rubert_conversational_cased_sentiment/custom_config.json)
model(["Сегодня хорошая погода", "Я счастлив проводить с тобою время", "Мне нравится эта музыкальная композиция"])

```


