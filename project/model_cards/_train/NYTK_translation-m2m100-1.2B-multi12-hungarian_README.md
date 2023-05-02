---
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
license: mit
metrics:
- sacrebleu
- chrf
widget:
- text: >-
    This may not make much sense to you, sir, but I'd like to ask your
    permission to date your daughter.
---

# Hungarian-centered 12-lingual finetuned M2M100_1.2B model

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
@article{laki-yang-12lang,
    title = {Solving Hungarian natural language processing tasks with multilingual generative models},
	journal = {Annales Mathematicae et Informaticae},
	year = {2023},
	author = {Yang, Zijian Győző and Laki László János},
	pages = {in press}
}

```