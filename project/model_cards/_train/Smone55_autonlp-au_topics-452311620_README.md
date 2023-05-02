---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Smone55/autonlp-data-au_topics
co2_eq_emissions: 208.0823957145878
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 452311620
- CO2 Emissions (in grams): 208.0823957145878

## Validation Metrics

- Loss: 0.5259971022605896
- Accuracy: 0.8767479025169796
- Macro F1: 0.8618813750734912
- Micro F1: 0.8767479025169796
- Weighted F1: 0.8742964006840133
- Macro Precision: 0.8627700506991158
- Micro Precision: 0.8767479025169796
- Weighted Precision: 0.8755603985289852
- Macro Recall: 0.8662183006750934
- Micro Recall: 0.8767479025169796
- Weighted Recall: 0.8767479025169796


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Smone55/autonlp-au_topics-452311620
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Smone55/autonlp-au_topics-452311620", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Smone55/autonlp-au_topics-452311620", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```