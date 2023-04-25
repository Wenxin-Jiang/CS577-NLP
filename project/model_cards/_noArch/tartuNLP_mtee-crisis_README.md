---
language: 
- et
- en
- de
- ru
tags:
- translation
- modularNMT
- fairseq
- MTee
- crisis
inference: false
---

# MTee translation model for crisis domain

A crisis (mostly healthcare-related) domain translation model for the MTee machine translation platform. The platform was developed in 2021 as a collaboration between the [TartuNLP](https://tartunlp.ai), the NLP research group at the University of Tartu, and [Tilde](https://tilde.com). More information about the project can be found [here](https://github.com/Project-MTee/mtee-platform/wiki).

The model uses a modular architecture, where each language has its own encoder and decoder that is used for all translation directions. The model can be used with our custom version of [FairSeq](https://github.com/TartuNLP/fairseq) and it is compatible with the [MTee](https://github.com/Project-MTee) platform and its [NMT workers](https://github.com/Project-MTee/translation-worker). Additionally, it is fully compatible with TartuNLP's  translation API components ([API](https://github.com/TartuNLP/translation-api) and [NMT workers](https://github.com/TartuNLP/translation-worker)).

Supported translation directions: `et-en`, `en-et`, `et-de`, `de-et`, `et-ru`, `ru-et`.

| Included files:          |             |
| ----------- | ----------- |
| Fairseq translation model | `modular_model.pt` |
| SentecePiece models | `sp-model.{lang}.model` |
| translation model vocabularies | `dict.{lang}.txt` |
