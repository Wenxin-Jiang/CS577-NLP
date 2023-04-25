---
tags:
- flair
- token-classification
- sequence-tagger-model
language: de
widget:
- text: "Herr Oberst Brunner ist nämlich Hauptagent für den Kanton Zürich."
license: mit
---

# Triple E - Effective Ensembling of Embeddings and Language Models for NER of Historical German

Based on [our paper](http://ceur-ws.org/Vol-2696/paper_173.pdf) we release a new baseline model for the German
[CLEF-HIPE shared task](https://impresso.github.io/CLEF-HIPE-2020/).

In contrast to the models used in the paper, we manually sentence-segmented and normalize hyphenations and
trained a NER model using the German Europeana BERT model.

Additionally, we perform experiments with different context sizes. This approach is described in
more detail in [this paper](https://arxiv.org/abs/2011.06993).

# Results

The results with different context sizes can be seen in the following table:

| Model                      | Run 1           | Run 2           | Run 3           | Run 4               | Run 5           | Avg.
| -------------------------- | --------------- | --------------- | --------------- | ------------------- | --------------- | ---------------
| German Europeana BERT      | (81.45) / 76.92 | (**81.53**) / 77.03 | (80.49) / 77.83 | (80.88) / 77.19 | (81.39) / 77.00 | (81.15 ± 0.45) / 77.19 ± 0.34
| German Europeana BERT (16) | (**82.56**) / 77.38 | (81.19) / 77.76 | (80.99) / 76.34 | (81.27) / 77.70 | (81.28) / 77.22 | (81.46 ± 0.63) / 77.28 ± 0.57
| German Europeana BERT (32) | (**82.04**) / 78.50 | (81.14) / 76.56 | (81.81) / 78.28 | (81.50) / 76.90 | (81.64) / 77.94 | (81.63 ± 0.34) / 77.64 ± 0.86
| German Europeana BERT (64) | (81.21) / 78.39 | (81.27) / 75.98 | (**81.88**) / 78.40 | (81.66) / 77.35 | (81.29) / 76.70 | (81.46 ± 0.29) / 77.36 ± 1.06
| German Europeana BERT (80) | (82.13) / 77.77 | (81.31) / 76.81 | (82.09) / 78.69 | (**82.30**) / 76.79 | (80.65) / 77.10 | (81.70 ± 0.70) / 77.43 ± 0.81

For model upload, we choose the best model on development score: 82.56 with a context length of 16.

## Comparisons

The following figure shows the results with different context sized (on development dataset):

![German CLEF-HIPE Development Results](figures/clef_hipe_f1_score_development.png)

We perform "Almost Stochastic Order" tests as proposed in the
["Deep Dominance - How to Properly Compare Deep Neural Models"](https://www.aclweb.org/anthology/P19-1266/) paper.
The heatmap figure is heavily inspired by the ["CharacterBERT"](https://arxiv.org/abs/2010.10392) paper.

![Almost Stochastic Order Tests on Development set](figures/clef_hipe_asd_development.png)
