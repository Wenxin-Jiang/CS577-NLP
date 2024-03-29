---
license: apache-2.0
language:
- hu
tags:
- text-classification
metrics:
- accuracy
widget:
- text: >-
    Kovácsné Nagy Erzsébet [SEP] A Kovácsné Nagy Erzsébet nagyon jól érzi magát
    a Nokiánál, azonban a Németországból érkezett Kovács Péter nehezen boldogul
    a beilleszkedéssel.
  example_title: positive
- text: >-
    Kovács Péter [SEP] A Kovácsné Nagy Erzsébet nagyon jól érzi magát a
    Nokiánál, azonban a Németországból érkezett Kovács Péter nehezen boldogul a
    beilleszkedéssel.
  example_title: negative
- text: >-
    Kovácsné Nagy Erzsébet [SEP] A Kovácsné Nagy Erzsébet azt mondta, hogy a
    Németországból érkezett Kovács Péter nehezen boldogul a beilleszkedéssel.
  example_title: neutral
---

# Hungarian Aspect-based Sentiment Analysis with finetuned huBERT model

For further models, scripts and details, see [our repository](https://github.com/nytud/sentiment-analysis) or [our demo site](https://juniper.nytud.hu/demo/nlp).

  - Pretrained model used: huBERT
  - Finetuned on OpinHuBank (OHB) Corpus
  - Labels: 0 (negative), 1 (neutral), 2 (positive)
  - Separator: [SEP]
  	
## Limitations

- max_seq_length = 256

## Results

| Model | OHB | 
| ------------- | ------------- | 
| huBERT | **82.30**  |
| XLM-R | 80.59  |

## Usage with pipeline

```python
from transformers import pipeline

classification = pipeline(task="sentiment-analysis", model="NYTK/sentiment-ohb3-hubert-hungarian")
input_text = "Kovácsné Nagy Erzsébet [SEP] A Kovácsné Nagy Erzsébet nagyon jól érzi magát a Nokiánál, azonban a Németországból érkezett Kovács Péter nehezen boldogul a beilleszkedéssel."

print(classification(input_text)[0])
```

## Citation
If you use this model, please cite the following paper:

```
@inproceedings {yang-asent,
    title = {Neurális entitásorientált szentimentelemző alkalmazás magyar nyelvre},
	booktitle = {XIX. Magyar Számítógépes Nyelvészeti Konferencia (MSZNY 2023)},
	year = {2023},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Hungary},
	author = {Yang, Zijian Győző and Laki, László János},
	pages = {107--117}
}
```