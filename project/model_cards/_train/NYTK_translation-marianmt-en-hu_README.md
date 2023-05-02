---

language: 
  - en
  - hu
tags:
- translation
license: gpl-3.0
metrics:
- sacrebleu
- chrf
widget:
- text: "This may not make much sense to you, sir, but I'd like to ask your permission to date your daughter."
  example_title: "Translation: English-Hungarian"

---

# Marian Translation model

For further models, scripts and details, see [our repository](https://github.com/nytud/machine-translation) or [our demo site](https://juniper.nytud.hu/demo/nlp). There is a description of the REST API of our service.

This model has been traind with a [MarianNMT](https://github.com/marian-nmt/marian-dev) v1.10.23; commit: 42f0b8b7 transformer-big typed environment.
This repository contains our translation model (en-hu) which were published in MSZNY 2022 conference.


- Source language: English
- Target language: Hungarian

- Pretrained on subcorpora from OPUS
	- Segments: 56.837.602

## Limitations

## Results

| Model | BLEU | chrF-3 |
| ------------- | ------------- | ------------- |
| Google en-hu  | 25.30  | 54.08 |
| **Marian-big-enhu** | **37.30**  | **61.61** |

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
