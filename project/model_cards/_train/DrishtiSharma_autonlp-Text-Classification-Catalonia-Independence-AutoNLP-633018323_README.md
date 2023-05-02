---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- DrishtiSharma/autonlp-data-Text-Classification-Catalonia-Independence-AutoNLP
co2_eq_emissions: 3.622203603306694
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 633018323
- CO2 Emissions (in grams): 3.622203603306694

## Validation Metrics

- Loss: 0.681106686592102
- Accuracy: 0.709136109384711
- Macro F1: 0.6987186860138147
- Micro F1: 0.709136109384711
- Weighted F1: 0.7059639788836748
- Macro Precision: 0.7174345617951404
- Micro Precision: 0.709136109384711
- Weighted Precision: 0.712710833401347
- Macro Recall: 0.6912117894374218
- Micro Recall: 0.709136109384711
- Weighted Recall: 0.709136109384711


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/DrishtiSharma/autonlp-Text-Classification-Catalonia-Independence-AutoNLP-633018323
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("DrishtiSharma/autonlp-Text-Classification-Catalonia-Independence-AutoNLP-633018323", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("DrishtiSharma/autonlp-Text-Classification-Catalonia-Independence-AutoNLP-633018323", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```