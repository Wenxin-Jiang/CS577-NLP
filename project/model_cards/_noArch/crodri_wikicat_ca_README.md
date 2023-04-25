---
tags:
- autotrain
- text-classification
language:
- ca
widget:
- text: "Aquest dissabte, Francesc Solé va arribar a la meta a Ordino com el guanyador del Ultra Trail d'Andorra després de 170km amb un desnivell altitudinal de 13 500 metres, en un temps de 31 hores i 9 minuts."
- text: "Una cançó és una composició musical que conté, a vegades, una part amb veu o melodia vocal, és a dir, amb text, cantada, però també pot ser simplement un conjunt de notes tocades sistemàticament, formant un ritme."
datasets:
- projecte-aina/WikiCAT_ca
co2_eq_emissions:
  emissions: 47.543878831739285
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 2036166932
- CO2 Emissions (in grams): 47.5439

## Validation Metrics

- Loss: 0.701
- Accuracy: 0.787
- Macro F1: 0.776
- Micro F1: 0.787
- Weighted F1: 0.784
- Macro Precision: 0.786
- Micro Precision: 0.787
- Weighted Precision: 0.788
- Macro Recall: 0.775
- Micro Recall: 0.787
- Weighted Recall: 0.787


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/crodri/autotrain-wikicat_ca-2036166932
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("crodri/wikicat_ca", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("crodri/wikicat_ca", use_auth_token=True)

inputs = tokenizer("Una cançó és una composició musical que conté, a vegades, una part amb veu o melodia vocal, és a dir, amb text, cantada, però també pot ser simplement un conjunt de notes tocades sistemàticament, formant un ritme.", return_tensors="pt")

outputs = model(**inputs)
```