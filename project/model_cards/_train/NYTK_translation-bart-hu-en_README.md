---
language:
- hu
- en
tags:
- translation
license: apache-2.0
metrics:
- sacrebleu
- chrf
widget:
- text: >-
    Szeretném megragadni az alkalmat uram, hogy az engedélyét kérjem, hogy
    találkozhassak a lányával.
---

# BART Translation model

For further models, scripts and details, see [our repository](https://github.com/nytud/machine-translation) or [our demo site](https://juniper.nytud.hu/demo/nlp).

- Source language: Hungarian
- Target language: English

- Pretrained on English WikiText-103 and Hungarian Wikipedia
- Finetuned on subcorpora from OPUS
	- Segments: 56.837.602

## Limitations

- tokenized input text (tokenizer: [HuSpaCy](https://huggingface.co/huspacy))

## Results

| Model | BLEU | chrF-3 |
| ------------- | ------------- | ------------- |
| Google en-hu  | 25.30  | 54.08 |
| **BART-base-enhu** | **34.38**  | **58.88** |
| Google hu-en| 34.48  | 59.59 |
| **BART-base-huen** | **38.03** | **61,37** |

## Citation
If you use this model, please cite the following paper:
```
@inproceedings {yang-bart,
    title = {{BARTerezzünk! - Messze, messze, messze a világtól, - BART kísérleti modellek magyar nyelvre}},
	booktitle = {XVIII. Magyar Számítógépes Nyelvészeti Konferencia},
	year = {2022},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Magyarország},
	author = {Yang, Zijian Győző},
	pages = {15--29}
}

```