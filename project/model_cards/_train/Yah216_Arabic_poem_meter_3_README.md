---
---
language: ar
widget:
 - text: "قفا نبك من ذِكرى حبيب ومنزلِ  بسِقطِ اللِّوى بينَ الدَّخول فحَوْملِ"
 - text: "سَلو قَلبي غَداةَ سَلا وَثابا لَعَلَّ عَلى الجَمالِ لَهُ عِتابا"
co2_eq_emissions: 404.66986451902227
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- CO2 Emissions (in grams): 404.66986451902227
## Dataset
We used the APCD dataset cited hereafter for pretraining the model. The dataset has been cleaned and only the main text and the meter columns were kept:
```
@Article{Yousef2019LearningMetersArabicEnglish-arxiv,
  author =       {Yousef, Waleed A. and Ibrahime, Omar M. and Madbouly, Taha M. and Mahmoud,
                  Moustafa A.},
  title =        {Learning Meters of Arabic and English Poems With Recurrent Neural Networks: a Step
                  Forward for Language Understanding and Synthesis},
  journal =      {arXiv preprint arXiv:1905.05700},
  year =         2019,
  url =          {https://github.com/hci-lab/LearningMetersPoems}
}
```
## Validation Metrics

- Loss: 0.21315555274486542
- Accuracy: 0.9493554089595999
- Macro F1: 0.7537353091512587

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "قفا نبك من ذِكرى حبيب ومنزلِ  بسِقطِ اللِّوى بينَ الدَّخول فحَوْملِ"}' https://api-inference.huggingface.co/models/Yah216/Arabic_poem_meter_3
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Yah216/Arabic_poem_meter_3", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Yah216/Arabic_poem_meter_3", use_auth_token=True)

inputs = tokenizer("قفا نبك من ذِكرى حبيب ومنزلِ  بسِقطِ اللِّوى بينَ الدَّخول فحَوْملِ", return_tensors="pt")

outputs = model(**inputs)
```