---
tags: autotrain
language: unk
widget:
- text: "Climate Change is a hoax"
- text: "It is freezing, where is global warming"
datasets:
- KeithHorgan98/autotrain-data-TweetClimateAnalysis
co2_eq_emissions: 133.19491276284793
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 678720226
- CO2 Emissions (in grams): 133.19491276284793

## Validation Metrics

- Loss: 0.4864234924316406
- Accuracy: 0.865424430641822
- Macro F1: 0.7665472174344069
- Micro F1: 0.8654244306418221
- Weighted F1: 0.8586375445115083
- Macro Precision: 0.8281449061702826
- Micro Precision: 0.865424430641822
- Weighted Precision: 0.8619727477790186
- Macro Recall: 0.736576343905098
- Micro Recall: 0.865424430641822
- Weighted Recall: 0.865424430641822


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/KeithHorgan98/autotrain-TweetClimateAnalysis-678720226
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("KeithHorgan98/autotrain-TweetClimateAnalysis-678720226", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("KeithHorgan98/autotrain-TweetClimateAnalysis-678720226", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```