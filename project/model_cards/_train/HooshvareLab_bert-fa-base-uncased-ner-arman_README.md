---
language: fa
license: apache-2.0
---

# ParsBERT (v2.0)
A Transformer-based Model for Persian Language Understanding

We reconstructed the vocabulary and fine-tuned the ParsBERT v1.1 on the new Persian corpora in order to provide some functionalities for using ParsBERT in other scopes!
Please follow the [ParsBERT](https://github.com/hooshvare/parsbert) repo for the latest information about previous and current models.


## Persian NER [ARMAN, PEYMA]

This task aims to extract named entities in the text, such as names and label with appropriate `NER` classes such as locations, organizations, etc. The datasets used for this task contain sentences that are marked with `IOB` format. In this format, tokens that are not part of an entity are tagged as `”O”` the `”B”`tag corresponds to the first word of an object, and the `”I”` tag corresponds to the rest of the terms of the same entity. Both `”B”` and `”I”` tags are followed by a hyphen (or underscore), followed by the entity category. Therefore, the NER task is a multi-class token classification problem that labels the tokens upon being fed a raw text. There are two primary datasets used in Persian NER, `ARMAN`, and `PEYMA`.


### ARMAN

ARMAN dataset holds 7,682 sentences with 250,015 sentences tagged over six different classes.

1. Organization
2. Location
3. Facility
4. Event
5. Product
6. Person


|     Label    |   #   |
|:------------:|:-----:|
| Organization | 30108 |
|   Location   | 12924 |
|   Facility   |  4458 |
|     Event    |  7557 |
|    Product   |  4389 |
|    Person    | 15645 |

**Download**
You can download the dataset from [here](https://github.com/HaniehP/PersianNER)


## Results

The following table summarizes the F1 score obtained by ParsBERT as compared to other models and architectures.

| Dataset | ParsBERT v2 | ParsBERT v1 | mBERT | MorphoBERT | Beheshti-NER | LSTM-CRF | Rule-Based CRF | BiLSTM-CRF |
|---------|-------------|-------------|-------|------------|--------------|----------|----------------|------------|
| ARMAN   | 99.84*      | 98.79       | 95.89 | 89.9       | 84.03        | 86.55    | -              | 77.45      |


## How to use :hugs:

| Notebook     |      Description      |   |
|:----------|:-------------|------:|
| [How to use Pipelines](https://github.com/hooshvare/parsbert-ner/blob/master/persian-ner-pipeline.ipynb)  | Simple and efficient way to use State-of-the-Art models on downstream tasks through transformers | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hooshvare/parsbert-ner/blob/master/persian-ner-pipeline.ipynb) |


### BibTeX entry and citation info

Please cite in publications as the following:

```bibtex
@article{ParsBERT,
    title={ParsBERT: Transformer-based Model for Persian Language Understanding},
    author={Mehrdad Farahani, Mohammad Gharachorloo, Marzieh Farahani, Mohammad Manthouri},
    journal={ArXiv},
    year={2020},
    volume={abs/2005.12515}
}
```

## Questions?
Post a Github issue on the [ParsBERT Issues](https://github.com/hooshvare/parsbert/issues) repo.