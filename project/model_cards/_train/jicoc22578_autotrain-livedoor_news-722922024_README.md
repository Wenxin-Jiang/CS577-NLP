---
tags: autotrain
language: ja
widget:
- text: "Windows 11搭載PCを買ったら最低限やっておきたいこと"
- text: "3月デスクトップOSシェア、Windowsが増加しMacが減少"
- text: "raytrek、Core i7-12700HとRTX 3070 Tiを搭載するノートPC"
datasets:
- jicoc22578/autotrain-data-livedoor_news
co2_eq_emissions: 0.019299491458156143
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 722922024
- CO2 Emissions (in grams): 0.019299491458156143

## Validation Metrics

- Loss: 0.19609540700912476
- Accuracy: 0.9457627118644067
- Macro F1: 0.9404319054946133
- Micro F1: 0.9457627118644067
- Weighted F1: 0.9456037443251943
- Macro Precision: 0.9420917371721244
- Micro Precision: 0.9457627118644067
- Weighted Precision: 0.9457910238180336
- Macro Recall: 0.9391783746329772
- Micro Recall: 0.9457627118644067
- Weighted Recall: 0.9457627118644067


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/jicoc22578/autotrain-livedoor_news-722922024
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("jicoc22578/autotrain-livedoor_news-722922024", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("jicoc22578/autotrain-livedoor_news-722922024", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```