---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "Vull sentir una canço del Pets"
- text: "Com puc anar a l'estació de trens?"
- text: "afegeix a la llista de la compra un litre de llet"
datasets:
- crodri/autotrain-data-massive-4-catalan
co2_eq_emissions:
  emissions: 13.789236303098791
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2452075980
- CO2 Emissions (in grams): 13.7892

## Validation Metrics

- Loss: 0.546
- Accuracy: 0.882
- Macro F1: 0.855
- Micro F1: 0.882
- Weighted F1: 0.881
- Macro Precision: 0.862
- Micro Precision: 0.882
- Weighted Precision: 0.886
- Macro Recall: 0.858
- Micro Recall: 0.882
- Weighted Recall: 0.882


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/crodri/MassiveCatalanIntents
```

Or Python API:

```
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("crodri/MassiveCatalanIntents", use_auth_token=True)

model = AutoModelForSequenceClassification.from_pretrained("crodri/MassiveCatalanIntents", use_auth_token=True)

pipe = pipeline("text-classification",model=model,tokenizer=tokenizer)

result = pipe("afegeix a la llista de la compra un litre de llet")
```