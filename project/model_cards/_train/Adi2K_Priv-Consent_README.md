---

language: eng
widget:
- text: "You can control cookies and tracking tools. To learn how to manage how we - and our vendors - use cookies and other tracking tools, please click here."
datasets:
- Adi2K/autonlp-data-Priv-Consent
---

# Model

- Problem type: Binary Classification
- Model ID: 12592372

## Validation Metrics

- Loss: 0.23033875226974487
- Accuracy: 0.9138655462184874
- Precision: 0.9087136929460581
- Recall: 0.9201680672268907
- AUC: 0.9690346726926065
- F1: 0.9144050104384133

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Adi2K/autonlp-Priv-Consent-12592372
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Adi2K/autonlp-Priv-Consent-12592372", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Adi2K/autonlp-Priv-Consent-12592372", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```