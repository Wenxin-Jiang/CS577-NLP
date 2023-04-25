---
language: eu
license: cc-by-nc-4.0
tags:
- basque
- roberta
---

# Roberta-eus cc100 base cased

This is a RoBERTa model for Basque model presented in [Does corpus quality really matter for low-resource languages?](https://arxiv.org/abs/2203.08111). There are several models for Basque using the RoBERTa architecture, using different corpora:

- roberta-eus-euscrawl-base-cased: Basque RoBERTa model trained on Euscrawl, a corpus created using tailored crawling from Basque sites. EusCrawl contains 12,528k documents and 423M tokens.
- roberta-eus-euscrawl-large-cased: RoBERTa large trained on EusCrawl.
- roberta-eus-mC4-base-cased: Basque RoBERTa model trained on the Basque portion of mc4 dataset.
- roberta-eus-CC100-base-cased: Basque RoBERTa model trained on  Basque portion of cc100 dataset.

The models have been tested on five different downstream tasks for Basque: Topic classification, Sentiment analysis, Stance detection, Named Entity Recognition (NER), and Question Answering (refer to the [paper](https://arxiv.org/abs/2203.08111) for more details). See summary of results below:


| Model                            | Topic class. | Sentiment | Stance det. |     NER  |     QA   | Average  |
|----------------------------------|--------------|-----------|-------------|----------|----------|----------|
| roberta-eus-euscrawl-base-cased  |         76.2 |      77.7 |        57.4 |    86.8  |    34.6  |    66.5  |
| roberta-eus-euscrawl-large-cased |     **77.6** |      78.8 |        62.9 | **87.2** | **38.3** | **69.0** |
| roberta-eus-mC4-base-cased       |         75.3 |  **80.4** |        59.1 |    86.0  |    35.2  |    67.2  |
| roberta-eus-CC100-base-cased     |         76.2 |      78.8 |    **63.4** |    85.2  |    35.8  |    67.9  |


If you use any of these models, please cite the following paper:

```
@misc{artetxe2022euscrawl,
 title={Does corpus quality really matter for low-resource languages?},
 author={Mikel Artetxe, Itziar Aldabe, Rodrigo Agerri,
         Olatz Perez-de-Viñaspre, Aitor Soroa},
 year={2022},
 eprint={2203.08111},
 archivePrefix={arXiv},
 primaryClass={cs.CL}
}
```
