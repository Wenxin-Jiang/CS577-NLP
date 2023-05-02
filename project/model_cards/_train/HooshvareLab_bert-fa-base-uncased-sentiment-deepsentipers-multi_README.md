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



### DeepSentiPers

which is a balanced and augmented version of SentiPers, contains 12,138 user opinions about digital products labeled with five different classes; two positives (i.e., happy and delighted), two negatives (i.e., furious and angry) and one neutral class. Therefore, this dataset can be utilized for both multi-class and binary classification. In the case of binary classification, the neutral class and its corresponding sentences are removed from the dataset.

**Binary:**
1. Negative (Furious + Angry)
2. Positive (Happy + Delighted)

**Multi**
1. Furious
2. Angry
3. Neutral
4. Happy
5. Delighted


|   Label   |   #  |
|:---------:|:----:|
|  Furious  |  236 |
|   Angry   | 1357 |
|  Neutral  | 2874 |
|   Happy   | 2848 |
| Delighted | 2516 |



**Download**
You can download the dataset from:

- [SentiPers](https://github.com/phosseini/sentipers)
- [DeepSentiPers](https://github.com/JoyeBright/DeepSentiPers)

## Results

The following table summarizes the F1 score obtained by ParsBERT as compared to other models and architectures.

|          Dataset         | ParsBERT v2 | ParsBERT v1 | mBERT | DeepSentiPers |
|:------------------------:|:-----------:|:-----------:|:-----:|:-------------:|
|  SentiPers (Multi Class) |    71.31*   |    71.11    |   -   |     69.33     |
| SentiPers (Binary Class) |    92.42*   |    92.13    |   -   |     91.98     |


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