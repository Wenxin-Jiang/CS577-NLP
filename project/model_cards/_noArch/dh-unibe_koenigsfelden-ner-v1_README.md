---
license: mit
tags:
- flair
- token-classification
- sequence-tagger-model
language: de
widget:
- text: "ab dryn matten, gelegen ze Niderlentz, hinden in langen matten eychen, waren ze etlichen zitten Jennis Huͤbers von Niderlentz, und hat sie gekoͧft von Walther Renold"
---

# Königsfelden NER

A model for historical German developed by Ismail Prada Ziegler as part of a research project at the University of Bern, Digital Humanities.


## Performance

| | PER | ORG | LOC | Micro-Avg |
| :---: | :---: | :---: | :---: | :---: |
| Precision | 88.76% | 69.01% | 81.96% | 84.19% |
| Recall | 88.99% | 62.97% | 85.10% | 84.02% |
| F1-Score | 88.88% | 65.85% | 83.50% | 84.10% |
 

## Data Set

[Königsfelden Charters](https://zenodo.org/record/5179361), 14th-17th Century, Early New High German, 623k tokens training, dev, test data.


## Notice

This model was a prototype with no extensive experimenting, better results can be likely be achieved on this dataset.

The documents in the dataset are published [here](https://www.koenigsfelden.uzh.ch).

