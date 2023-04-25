---
language: 
- et
- en
- de
- ru
- fi
- lt
- lv
tags:
- translation
- modularNMT
- fairseq
inference: false
---
# A Modular Translation Model for 7 Languages

This model supports translation in all directions between the following languages: et, en, de, ru, fi, lt, lv.

The model uses a modular architecture, where each language has its own encoder and decoder that is used for all translation direction combinations. The model can be used with our custom version of [FairSeq](https://github.com/TartuNLP/fairseq) and with our translation API components ([API](https://github.com/TartuNLP/translation-api) and [NMT workers](https://github.com/TartuNLP/translation-worker)). Additionally, it is fully compatible with the [MTee](https://github.com/Project-MTee) platform and its [NMT workers](https://github.com/Project-MTee/translation-worker).


| Files: |             |
| ----------- | ----------- |
| Fairseq translation model | `modular_model.pt` |
| SentecePiece models | `sp-model.{lang}.model` |
| translation model vocabularies | `dict.{lang}.txt` |