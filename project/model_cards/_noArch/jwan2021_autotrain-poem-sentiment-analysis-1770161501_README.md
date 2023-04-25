---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- jwan2021/autotrain-data-poem-sentiment-analysis
co2_eq_emissions:
  emissions: 1.6081724212150736
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
  - Text Sentiment Analysis: Positive, Neutral, Negative
- Model ID: 1770161501
- CO2 Emissions (in grams): 1.6082

## Validation Metrics

- Loss: 0.599
- Accuracy: 0.821
- Macro F1: 0.677
- Micro F1: 0.821
- Weighted F1: 0.814
- Macro Precision: 0.741
- Micro Precision: 0.821
- Weighted Precision: 0.825
- Macro Recall: 0.683
- Micro Recall: 0.821
- Weighted Recall: 0.821


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/jwan2021/autotrain-poem-sentiment-analysis-1770161501
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161501", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161501", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```