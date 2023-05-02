---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Rem59/autotrain-data-Test_2
co2_eq_emissions: 2.0134443204822188
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 789524315
- CO2 Emissions (in grams): 2.0134443204822188

## Validation Metrics

- Loss: 0.8042349815368652
- Accuracy: 0.6904761904761905
- Macro F1: 0.27230046948356806
- Micro F1: 0.6904761904761905
- Weighted F1: 0.5640509725016768
- Macro Precision: 0.23015873015873015
- Micro Precision: 0.6904761904761905
- Weighted Precision: 0.4767573696145125
- Macro Recall: 0.3333333333333333
- Micro Recall: 0.6904761904761905
- Weighted Recall: 0.6904761904761905


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Rem59/autotrain-Test_2-789524315
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Rem59/autotrain-Test_2-789524315", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Rem59/autotrain-Test_2-789524315", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```