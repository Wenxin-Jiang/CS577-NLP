---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- Ritvik19/autotrain-data-sentiment_polarity
co2_eq_emissions: 4.280488237750762
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 918130222
- CO2 Emissions (in grams): 4.280488237750762

## Validation Metrics

- Loss: 0.13608604669570923
- Accuracy: 0.9504804036293305
- Precision: 0.9792047060317863
- Recall: 0.9647185343057701
- AUC: 0.9791895292939061
- F1: 0.9719076444852428

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Ritvik19/autotrain-sentiment_polarity-918130222
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Ritvik19/autotrain-sentiment_polarity-918130222", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Ritvik19/autotrain-sentiment_polarity-918130222", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```