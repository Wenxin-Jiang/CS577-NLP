---
language: fa
license: apache-2.0
---

# ParsBERT (v2.0)
A Transformer-based Model for Persian Language Understanding


We reconstructed the vocabulary and fine-tuned the ParsBERT v1.1 on the new Persian corpora in order to provide some functionalities for using ParsBERT in other scopes!
Please follow the [ParsBERT](https://github.com/hooshvare/parsbert) repo for the latest information about previous and current models.


## Persian Text Classification [DigiMag, Persian News]

The task target is labeling texts in a supervised manner in both existing datasets `DigiMag` and `Persian News`.



### DigiMag

A total of 8,515 articles scraped from [Digikala Online Magazine](https://www.digikala.com/mag/). This dataset includes seven different classes.

1. Video Games
2. Shopping Guide
3. Health Beauty
4. Science Technology
5. General
6. Art Cinema
7. Books Literature


|        Label       |   #  |
|:------------------:|:----:|
|     Video Games    | 1967 |
|   Shopping Guide   |  125 |
|    Health Beauty   | 1610 |
| Science Technology | 2772 |
|       General      |  120 |
|     Art Cinema     | 1667 |
|  Books Literature  |  254 |


**Download**
You can download the dataset from [here](https://drive.google.com/uc?id=1YgrCYY-Z0h2z0-PfWVfOGt1Tv0JDI-qz)


## Results

The following table summarizes the F1 score obtained by ParsBERT as compared to other models and architectures.

|      Dataset      | ParsBERT v2 | ParsBERT v1 | mBERT |
|:-----------------:|:-----------:|:-----------:|:-----:|
| Digikala Magazine |    93.65*   |    93.59    | 90.72 |



## How to use :hugs:

| Task                | Notebook                                                                                                                                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Text Classification | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hooshvare/parsbert/blob/master/notebooks/Taaghche_Sentiment_Analysis.ipynb) |


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