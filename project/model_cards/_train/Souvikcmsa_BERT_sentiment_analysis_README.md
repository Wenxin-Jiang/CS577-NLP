---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
- Output: "Positive"
datasets:
- Souvikcmsa/autotrain-data-sentiment_analysis
co2_eq_emissions: 0.029363397844935534
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification (3-class Sentiment Classification)

## Validation Metrics
If you search sentiment analysis model in huggingface you find a model from finiteautomata. Their model provides micro and macro F1 score around 67%. Check out this model with around 80% of macro and micro F1 score. 
- Loss: 0.4992932379245758
- Accuracy: 0.799017824663514
- Macro F1: 0.8021508522962549
- Micro F1: 0.799017824663514
- Weighted F1: 0.7993775463659935
- Macro Precision: 0.80406197665167
- Micro Precision: 0.799017824663514
- Weighted Precision: 0.8000374433849405
- Macro Recall: 0.8005261994732908
- Micro Recall: 0.799017824663514
- Weighted Recall: 0.799017824663514


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Souvikcmsa/autotrain-sentiment_analysis-762923428
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Souvikcmsa/autotrain-sentiment_analysis-762923428", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Souvikcmsa/autotrain-sentiment_analysis-762923428", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```
OR
```
from transformers import pipeline

classifier = pipeline("text-classification", model = "Souvikcmsa/BERT_sentiment_analysis")
classifier("I loved Star Wars so much!")# Positive
classifier("A soccer game with multiple males playing. Some men are playing a sport.")# Neutral
```