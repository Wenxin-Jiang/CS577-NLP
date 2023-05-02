---
tags: autotrain
language: en
widget:
- text: "Jerimee"
  example_title: "a weird human name"
- text: "Curtastica"
  example_title: "a goblin name"
- text: "Fatima"
  example_title: "a common human name"
datasets:
- Jerimee/autotrain-data-dontknowwhatImdoing
co2_eq_emissions: 0.012147398577917884
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 980432459
- CO2 Emissions (in grams): 0.012147398577917884

## Validation Metrics

- Loss: 0.0469294898211956
- Accuracy: 0.9917355371900827
- Precision: 0.9936708860759493
- Recall: 0.9936708860759493
- AUC: 0.9990958408679927
- F1: 0.9936708860759493

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Jerimee/autotrain-dontknowwhatImdoing-980432459
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Jerimee/autotrain-dontknowwhatImdoing-980432459", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Jerimee/autotrain-dontknowwhatImdoing-980432459", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```