---
tags: autonlp
language: en
widget:
- text: "Not Many People Know About The City 1200 Feet Below Detroit"
- text: "Bob accepts the challenge, and the next week they're standing in Saint Peters square. 'This isnt gonna work, he's never going to see me here when theres this much people. You stay here, I'll go talk to him and you'll see me on the balcony, the guards know me too.' Half an hour later, Bob and the pope appear side by side on the balcony. Bobs boss gets a heart attack, and Bob goes to visit him in the hospital."
- text: "I’m sorry if you made it this far, but I’m just genuinely idk, I feel like I shouldn’t give up, it’s just getting harder to come back from stuff like this."
datasets:
- akilesh96/autonlp-data-mrcooper_text_classification
co2_eq_emissions: 5.999771405025692
---

# Model Trained Using AutoNLP

- Problem type: Multi-class Classification
- Model ID: 529614927
- CO2 Emissions (in grams): 5.999771405025692

## Validation Metrics

- Loss: 0.7582379579544067
- Accuracy: 0.7636103151862464
- Macro F1: 0.770630619486531
- Micro F1: 0.7636103151862464
- Weighted F1: 0.765233270165301
- Macro Precision: 0.7746285216467107
- Micro Precision: 0.7636103151862464
- Weighted Precision: 0.7683270753840836
- Macro Recall: 0.7680576576961138
- Micro Recall: 0.7636103151862464
- Weighted Recall: 0.7636103151862464


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/akilesh96/autonlp-mrcooper_text_classification-529614927
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("akilesh96/autonlp-mrcooper_text_classification-529614927", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("akilesh96/autonlp-mrcooper_text_classification-529614927", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```