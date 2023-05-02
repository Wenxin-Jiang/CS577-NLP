---
language: en
tags:
- scibert
- token-classification
- medical-domain
metrics:
- f1
- precision
- recall
dataset:
- Mathking/primary_outcomes
widget:
- text: "The FIRST primary outcome is pain at 12 months as measured by the VAS. The primary analysis is to assess whether surgical correction "
  example_title: "PubMed Article : Methods section"
---

# Scibert Finetuned for Primary Outcomes extraction in Biomedical Text


## Model description
SciBERT (Scivocab Uncased Version) finetuned on dataset from A. Koroleva ).
This model is trained to detect primary outcomes (token classification) in biomedical articles.

## Intended uses & limitations
This model was trained to detect primary outcomes in medical articles.

## Training data
[Dataset from A. Koroleva](https://zenodo.org/record/3234811#.YnodlVzP2EI)

## Evaluation results
Here are the results from the different models evaluated. Evaluation is done using 10-fold cross validation using the 10 splits originally defined in the dataset.

|    | model                    |       f1 |   precision |   recall |
|---:|:-------------------------|---------:|------------:|---------:|
|  1 | biobert-v1.1             | 0.873347 |    0.870358 | 0.878657 |
|  2 | scibert_scivocab_uncased | 0.870242 |    0.863077 | 0.879617 |
|  3 | biobert_v1.0_pubmed_pmc  | 0.863499 |    0.858515 | 0.8713   |
|  4 | scibert_scivocab_cased   | 0.85848  |    0.859122 | 0.862749 |
