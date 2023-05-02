---
language: ar

datasets:
- Yah216/Poem_Rawiy_detection
co2_eq_emissions: 1.8046766441629636
widget:
 - "سَلو قَلبي غَداةَ سَلا وَثابا لَعَلَّ عَلى الجَمالِ لَهُ عِتاب"
---

# Model

- Problem type: Multi-class Classification
- CO2 Emissions (in grams): 1.8046766441629636

## Dataset
We used the APCD dataset cited hereafter for pretraining the model. The dataset has been cleaned and only the main text and the Qafiyah column were kept:
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

- Loss: 0.398613303899765
- Accuracy: 0.912351981006084
- Macro F1: 0.717311758991278
- Micro F1: 0.912351981006084
- Weighted F1: 0.9110094798809955


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/Yah216/Poem_Rawiy_detection
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Yah216/Poem_Qafiyah_Detection", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Yah216/Poem_Qafiyah_Detection", use_auth_token=True)

inputs = tokenizer("text, return_tensors="pt")

outputs = model(**inputs)
```