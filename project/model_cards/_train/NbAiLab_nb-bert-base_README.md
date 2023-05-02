---
language: no
license: cc-by-4.0
tags:
- norwegian
- bert
pipeline_tag: fill-mask
widget:
- text: På biblioteket kan du [MASK] en bok.
- text: Dette er et [MASK] eksempel.
- text: Av og til kan en språkmodell gi et [MASK] resultat. 
- text: Som ansat får du [MASK] for at bidrage til borgernes adgang til dansk kulturarv, til forskning og til samfundets demokratiske udvikling.
---
- **Release 1.1** (March 11, 2021)
- **Release 1.0** (January 13, 2021)

# NB-BERT-base

## Description

NB-BERT-base is a general BERT-base model built on the large digital collection at the National Library of Norway.

This model is based on the same structure as [BERT Cased multilingual model](https://github.com/google-research/bert/blob/master/multilingual.md), and is trained on a wide variety of Norwegian text (both bokmål and nynorsk) from the last 200 years.

## Intended use & limitations

The 1.1 version of the model is general, and should be fine-tuned for any particular use. Some fine-tuning sets may be found on GitHub, see

* https://github.com/NBAiLab/notram

## Training data

The model is trained on a wide variety of text. The training set is described on

* https://github.com/NBAiLab/notram

## More information

For more information on the model, see

https://github.com/NBAiLab/notram
