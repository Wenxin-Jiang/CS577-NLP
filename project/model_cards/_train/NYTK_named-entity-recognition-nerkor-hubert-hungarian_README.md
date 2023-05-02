---
language:
- hu
tags:
- token-classification
license: apache-2.0
metrics:
- f1
widget:
- text: >-
    A Kovácsné Nagy Erzsébet nagyon jól érzi magát a Nokiánál, azonban a
    Németországból érkezett Kovács Péter nehezen boldogul a beilleszkedéssel.
---

# Hungarian Named Entity Recognition Model with huBERT

For further models, scripts and details, see [our demo site](https://juniper.nytud.hu/demo/nlp).

  - Pretrained model used: SZTAKI-HLT/hubert-base-cc
  - Finetuned on [NYTK-NerKor](https://github.com/nytud/NYTK-NerKor)
  - NE categories are: PER, LOC, MISC, ORG
  	
## Limitations

- max_seq_length = 128

## Results

F-score: **90.18%**

## Usage with pipeline

```python
from transformers import pipeline

ner = pipeline(task="ner", model="NYTK/named-entity-recognition-nerkor-hubert-hungarian")
input_text = "A Kovácsné Nagy Erzsébet nagyon jól érzi magát a Nokiánál, azonban a Németországból érkezett Kovács Péter nehezen boldogul a beilleszkedéssel."

print(ner(input_text, aggregation_strategy="simple"))
```

## Citation
If you use this model, please cite the following paper:

```
@inproceedings {yang-language-models,
    title = {Training language models with low resources: RoBERTa, BART and ELECTRA experimental models for Hungarian},
	booktitle = {Proceedings of 12th IEEE International Conference on Cognitive Infocommunications (CogInfoCom 2021)},
	year = {2021},
	publisher = {IEEE},
	address = {Online},
	author = {Yang, Zijian Győző and Váradi, Tamás},
	pages = {279--285}
}

```