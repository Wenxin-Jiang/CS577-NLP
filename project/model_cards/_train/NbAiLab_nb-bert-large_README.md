---
language: no
license: cc-by-4.0
tags:
- norwegian
- bert
thumbnail: nblogo_3.png
pipeline_tag: fill-mask
widget:
- text: På biblioteket kan du låne en [MASK].
---

- **Release 1.0beta** (April 29, 2021)
 

# NB-BERT-large (beta)

## Description

NB-BERT-large is a general BERT-large model built on the large digital collection at the National Library of Norway.

This model is trained from scratch on a wide variety of Norwegian text (both bokmål and nynorsk) from the last 200 years using a monolingual Norwegian vocabulary.

## Intended use & limitations

The 1.0 version of the model is general, and should be fine-tuned for any particular use. Some fine-tuning sets may be found on Github, see

* https://github.com/NBAiLab/notram

## Training data

The model is trained on a wide variety of text. The training set is described on

* https://github.com/NBAiLab/notram

## More information

For more information on the model, see

https://github.com/NBAiLab/notram