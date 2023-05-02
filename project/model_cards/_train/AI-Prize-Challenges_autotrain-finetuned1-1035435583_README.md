---
tags: autotrain
language: zh
widget:
- text: "I love AutoTrain 🤗"
datasets:
- AI-Prize-Challenges/autotrain-data-finetuned1
co2_eq_emissions: 0.03608660562919794
---

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 1035435583
- CO2 Emissions (in grams): 0.03608660562919794

## Validation Metrics

- Loss: 0.31551286578178406
- Accuracy: 0.8816629547141797
- Precision: 0.8965702036441586
- Recall: 0.8906042054830983
- AUC: 0.9449180200540812
- F1: 0.8935772466283884

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/AI-Prize-Challenges/autotrain-finetuned1-1035435583
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("AI-Prize-Challenges/autotrain-finetuned1-1035435583", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("AI-Prize-Challenges/autotrain-finetuned1-1035435583", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```