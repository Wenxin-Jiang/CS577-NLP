---
language:
- en
- hu
tags:
- translation
license: apache-2.0
metrics:
- sacrebleu
- chrf
widget:
- text: >-
    This may not make much sense to you, sir, but I'd like to ask your
    permission to date your daughter.
  example_title: 'Translation: English-Hungarian'
---

# BART Translation model

For further models, scripts and details, see [our repository](https://github.com/nytud/machine-translation) or [our demo site](https://juniper.nytud.hu/demo/nlp).

- Source language: English
- Target language: Hungarian

- BART base model:
  - Pretrained on English WikiText-103 and Hungarian Wikipedia
  - Finetuned on subcorpora from OPUS
  	- Segments: 56.837.602

## Limitations

- tokenized input text (tokenizer: [HuSpaCy](https://huggingface.co/huspacy))
- max_source_length = 128
- max_target_length = 128

## Results

| Model | BLEU | chrF-3 | chrF-6 |
| ------------- | ------------- | ------------- | ------------- |
| Google | 25.30 | 54.09 | 49.0 |
| **BART** | **36.89** | **60.77** | **56.4** |
| mT5 | 27.69  | 53.73 | 48.57 |

## Citation
If you use this model, please cite the following paper:
```
@inproceedings {laki-yang-mt,
    title = {{Jobban fordítunk magyarra, mint a Google!}},
	booktitle = {XVIII. Magyar Számítógépes Nyelvészeti Konferencia},
	year = {2022},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Magyarország},
	author = {Laki, László and Yang, Zijian Győző},
	pages = {357--372}
}

```