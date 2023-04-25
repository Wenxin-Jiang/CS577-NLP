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
  emissions: 1.118838634517984
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1770161503
- CO2 Emissions (in grams): 1.1188

## Validation Metrics

- Loss: 0.562
- Accuracy: 0.804
- Macro F1: 0.583
- Micro F1: 0.804
- Weighted F1: 0.783
- Macro Precision: 0.559
- Micro Precision: 0.804
- Weighted Precision: 0.764
- Macro Recall: 0.610
- Micro Recall: 0.804
- Weighted Recall: 0.804


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/jwan2021/autotrain-poem-sentiment-analysis-1770161503
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161503", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161503", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```