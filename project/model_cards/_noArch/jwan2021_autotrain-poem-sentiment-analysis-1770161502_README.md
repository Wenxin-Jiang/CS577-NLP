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
  emissions: 0.9444638089570118
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1770161502
- CO2 Emissions (in grams): 0.9445

## Validation Metrics

- Loss: 0.589
- Accuracy: 0.799
- Macro F1: 0.580
- Micro F1: 0.799
- Weighted F1: 0.778
- Macro Precision: 0.554
- Micro Precision: 0.799
- Weighted Precision: 0.760
- Macro Recall: 0.609
- Micro Recall: 0.799
- Weighted Recall: 0.799


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/jwan2021/autotrain-poem-sentiment-analysis-1770161502
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161502", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161502", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```