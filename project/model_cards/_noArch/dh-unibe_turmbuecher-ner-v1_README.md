---
license: mit
tags:
- flair
- token-classification
- sequence-tagger-model
language: de
widget:
- text: "Namlich das Hanns Mulheim zer wirtshus zu Buchse sol gredt haben von Herren von Bern habind die von Zürich verratten oder wollend sy verratten."
---

# Turmbücher NER

A model for historical German developed by Ismail Prada Ziegler as part of a research project at the University of Bern, Digital Humanities.

## Performance

| | PER | ORG | LOC | Micro-Avg |
| :---: | :---: | :---: | :---: | :---: |
| Precision | 82.46% | 28.81% | 88.51% | 81.21% |
| Recall | 88.51% | 44.74% | 83.02% | 83.99% |
| F1-Score | 85.38% | 35.05% | 85.67% | 82.57% |

Note: ORG-tags were too inconsistent in the training data and performed poorly.

We discovered in first experiments that the model also performs reasonably well on automatically transcribed text (CER of around 5%). 

## Data Set

Main data set: [Berner Turmbücher](https://www.polit-forum-bern.ch/turmbuecher/), early volumes from 16th C., Early New High German, 61k tokens training data.

Secondary data sets:
- [SSRQ](https://www.ssrq-sds-fds.ch/home/) - Fribourg, language model + tagging, 59k tokens. 
- [Chorgerichtsmanuale](https://www.adfontes.uzh.ch/370540/training/deutsche-transkriptionsuebungen/chorgerichtsmanuale-einleitung) (unpublished), language model + tagging, 76k tokens.
- [Königsfelden Charters](https://www.koenigsfelden.uzh.ch/), language model, 623k tokens.
- Talgerichtsprotokolle (unpublished), language model, 438k tokens.

## Notice

This project is still in progress.

