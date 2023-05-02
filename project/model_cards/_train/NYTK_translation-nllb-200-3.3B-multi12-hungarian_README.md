---
license: cc-by-nc-4.0
language:
- hu
- bg
- cs
- de
- en
- hr
- pl
- ro
- ru
- sk
- sl
- sr
- uk
tags:
- translation
metrics:
- sacrebleu
- chrf
widget:
- text: >-
    This may not make much sense to you, sir, but I'd like to ask your
    permission to date your daughter.
---

# Hungarian-centered 12-lingual finetuned NLLB-200-3.3B model

For further details, see or [our demo site](https://juniper.nytud.hu/demo/nlp).

- Source language: Bulgarian (bg), Czech (cs), German (de), English (en), Croatian (hr), Polish, (pl), Romanian (ro), Russian (ru), Slovak (sk), Slovene (sl), Serbian (sr), Ukrainian (uk) 
- Target language: Hungarian (hu)

- Finetuned on subcorpora from OPUS
	- Segments: 3 million per language

## Limitations

- max_source_length: 256
- max_target_length: 256


## Citation
If you use this model, please cite the following paper:
```
@inproceedings {laki-yang-multi12,
    title = {Magyarcentrikus többnyelvű gépifordító rendszerek létrehozása},
	booktitle = {XIX. Magyar Számítógépes Nyelvészeti Konferencia (MSZNY 2023)},
	year = {2023},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Hungary},
	author = {Laki, László János and Yang, Zijian Győző},
	pages = {369--380}
}
```