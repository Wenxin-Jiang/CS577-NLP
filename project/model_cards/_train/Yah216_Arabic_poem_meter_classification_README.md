---
language: ar
widget:
 - text: "قفا نبك من ذِكرى حبيب ومنزلِ  بسِقطِ اللِّوى بينَ الدَّخول فحَوْملِ"
 - text: "سَلو قَلبي غَداةَ سَلا وَثابا لَعَلَّ عَلى الجَمالِ لَهُ عِتابا"

---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 913229914
- CO2 Emissions (in grams): 1.8892280988467902

## Validation Metrics

- Loss: 1.0592747926712036
- Accuracy: 0.6535535147098981
- Macro F1: 0.46508274468173677
- Micro F1: 0.6535535147098981
- Weighted F1: 0.6452975497424681
- Macro Precision: 0.6288501119526966
- Micro Precision: 0.6535535147098981
- Weighted Precision: 0.6818087199275457
- Macro Recall: 0.3910156950920188
- Micro Recall: 0.6535535147098981
- Weighted Recall: 0.6535535147098981


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Yah216/autotrain-poem_meter_classification-913229914
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Yah216/autotrain-poem_meter_classification-913229914", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Yah216/autotrain-poem_meter_classification-913229914", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```