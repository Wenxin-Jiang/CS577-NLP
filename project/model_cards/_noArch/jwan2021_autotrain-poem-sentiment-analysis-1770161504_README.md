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
  emissions: 1.463756126402436
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1770161504
- CO2 Emissions (in grams): 1.4638

## Validation Metrics

- Loss: 0.804
- Accuracy: 0.732
- Macro F1: 0.507
- Micro F1: 0.732
- Weighted F1: 0.715
- Macro Precision: 0.497
- Micro Precision: 0.732
- Weighted Precision: 0.702
- Macro Recall: 0.523
- Micro Recall: 0.732
- Weighted Recall: 0.732


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/jwan2021/autotrain-poem-sentiment-analysis-1770161504
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161504", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161504", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```