---
language: fa
license: apache-2.0
---

# ParsBERT (v2.0)
A Transformer-based Model for Persian Language Understanding

We reconstructed the vocabulary and fine-tuned the ParsBERT v1.1 on the new Persian corpora in order to provide some functionalities for using ParsBERT in other scopes!
Please follow the [ParsBERT](https://github.com/hooshvare/parsbert) repo for the latest information about previous and current models.


## Persian Sentiment [Digikala, SnappFood, DeepSentiPers]

It aims to classify text, such as comments, based on their emotional bias. We tested three well-known datasets for this task: `Digikala` user comments, `SnappFood` user comments, and `DeepSentiPers` in two binary-form and multi-form types.



### SnappFood

[Snappfood](https://snappfood.ir/) (an online food delivery company) user comments containing 70,000 comments with two labels (i.e. polarity classification): 

1. Happy
2. Sad

|   Label  |   #   |
|:--------:|:-----:|
| Negative | 35000 |
| Positive | 35000 |

**Download**
You can download the dataset from [here](https://drive.google.com/uc?id=15J4zPN1BD7Q_ZIQ39VeFquwSoW8qTxgu)

## Results

The following table summarizes the F1 score obtained by ParsBERT as compared to other models and architectures.

|          Dataset         | ParsBERT v2 | ParsBERT v1 | mBERT | DeepSentiPers |
|:------------------------:|:-----------:|:-----------:|:-----:|:-------------:|
|  SnappFood User Comments |    87.98    |    88.12*   | 87.87 |       -       |


## How to use :hugs:

| Task                | Notebook                                                                                                                                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sentiment Analysis | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hooshvare/parsbert/blob/master/notebooks/Taaghche_Sentiment_Analysis.ipynb) |


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