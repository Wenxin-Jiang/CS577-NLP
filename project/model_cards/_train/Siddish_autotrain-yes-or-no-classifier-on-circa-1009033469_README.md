---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Siddish/autotrain-data-yes-or-no-classifier-on-circa
co2_eq_emissions: 0.1287915253247826
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1009033469
- CO2 Emissions (in grams): 0.1287915253247826

## Validation Metrics

- Loss: 0.4084862470626831
- Accuracy: 0.8722054859679721
- Macro F1: 0.6340608446004876
- Micro F1: 0.8722054859679722
- Weighted F1: 0.8679846554644491
- Macro Precision: 0.645023001823007
- Micro Precision: 0.8722054859679721
- Weighted Precision: 0.8656545967138464
- Macro Recall: 0.6283763558287574
- Micro Recall: 0.8722054859679721
- Weighted Recall: 0.8722054859679721


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Siddish/autotrain-yes-or-no-classifier-on-circa-1009033469
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Siddish/autotrain-yes-or-no-classifier-on-circa-1009033469", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Siddish/autotrain-yes-or-no-classifier-on-circa-1009033469", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```