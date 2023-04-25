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
  emissions: 1.2662388515647711
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1770161500
- CO2 Emissions (in grams): 1.2662

## Validation Metrics

- Loss: 0.572
- Accuracy: 0.810
- Macro F1: 0.590
- Micro F1: 0.810
- Weighted F1: 0.787
- Macro Precision: 0.570
- Micro Precision: 0.810
- Weighted Precision: 0.766
- Macro Recall: 0.611
- Micro Recall: 0.810
- Weighted Recall: 0.810


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/jwan2021/autotrain-poem-sentiment-analysis-1770161500
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161500", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("jwan2021/autotrain-poem-sentiment-analysis-1770161500", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```