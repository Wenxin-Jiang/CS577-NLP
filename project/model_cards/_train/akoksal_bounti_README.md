---
language: "tr"
tags:
- sentiment
- twitter
- turkish
---

This Turkish Sentiment Analysis model is a fine-tuned checkpoint of pretrained [BERTurk model 128k uncased](https://huggingface.co/dbmdz/bert-base-turkish-128k-uncased) with [BounTi dataset](https://ieeexplore.ieee.org/document/9477814).
## Usage in Hugging Face Pipeline
```
from transformers import pipeline
bounti = pipeline("sentiment-analysis",model="akoksal/bounti")
print(bounti("Bu yemeği pek sevmedim"))
>> [{'label': 'negative', 'score': 0.8012508153915405}]
```

## Results
The scores of the finetuned model with BERTurk:

||Accuracy|Precision|Recall|F1|
|-------------|:---------:|:---------:|:------:|:-----:|
|Validation|0.745|0.706|0.730|0.715|
|Test|0.723|0.692|0.729|0.701|



## Dataset
You can find the dataset in [our Github repo](https://github.com/boun-tabi/BounTi-Turkish-Sentiment-Analysis) with the training, validation, and test splits.

Due to Twitter copyright, we cannot release the full text of the tweets. We share the tweet IDs, and the full text can be downloaded through official Twitter API.

|          | Training | Validation | Test |
|----------|:--------:|:----------:|:----:|
| Positive | 1691     |     188    |  469 |
| Neutral  | 3034     |     338    | 843  |
| Negative | 1008     |     113    | 280  |
| Total    | 5733     |     639    | 1592 |

## Citation
You can cite the following paper if you use our work:
```
@INPROCEEDINGS{BounTi,
  author={Köksal, Abdullatif and Özgür, Arzucan},
  booktitle={2021 29th Signal Processing and Communications Applications Conference (SIU)}, 
  title={Twitter Dataset and Evaluation of Transformers for Turkish Sentiment Analysis}, 
  year={2021},
  volume={},
  number={}
  }
```
---
