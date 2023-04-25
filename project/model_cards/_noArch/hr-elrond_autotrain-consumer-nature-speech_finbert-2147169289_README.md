---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- hr-elrond/autotrain-data-consumer-nature-speech_finbert
co2_eq_emissions:
  emissions: 0.004371975254312265
---


# Model Trained Using AutoTrain
We trained FinBERT to identify whether firms´ talk contains consumer concepts of human nature (e.g., "I believe consumers generally act rational.", "Consumers must take over responsibility for the choices they make.", "It seems consumers behave quite altruistic.") from statements that do not (e.g., "We expect buyers to double their purchases next year.", "We see a 5% growth in numbers compared to the previous year.").  
The training data consisted of 236 positive documents (containing concepts of consumer nature) and 1034 negative documents (not contain concepts of consumer nature) extracted from earnings call transcripts of S&P-500 companies (2015-2020).

# Model Trained Using AutoTrain

- Problem type: Binary Classification
- Model ID: 2147169289
- CO2 Emissions (in grams): 0.0044

## Validation Metrics

- Loss: 0.256
- Accuracy: 0.913
- Precision: 0.736
- Recall: 0.830
- AUC: 0.956
- F1: 0.780

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/hr-elrond/autotrain-consumer-nature-speech_finbert-2147169289
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("hr-elrond/autotrain-consumer-nature-speech_finbert-2147169289", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("hr-elrond/autotrain-consumer-nature-speech_finbert-2147169289", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```