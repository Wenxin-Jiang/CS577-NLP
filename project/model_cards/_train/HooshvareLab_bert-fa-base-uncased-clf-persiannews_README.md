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



### Persian News

A dataset of various news articles scraped from different online news agencies' websites. The total number of articles is 16,438, spread over eight different classes.

1. Economic
2. International
3. Political
4. Science Technology
5. Cultural Art
6. Sport
7. Medical


|        Label       |   #  |
|:------------------:|:----:|
|       Social       | 2170 |
|      Economic      | 1564 |
|    International   | 1975 |
|      Political     | 2269 |
| Science Technology | 2436 |
|    Cultural Art    | 2558 |
|        Sport       | 1381 |
|       Medical      | 2085 |


**Download**
You can download the dataset from [here](https://drive.google.com/uc?id=1B6xotfXCcW9xS1mYSBQos7OCg0ratzKC)


## Results

The following table summarizes the F1 score obtained by ParsBERT as compared to other models and architectures.

|      Dataset      | ParsBERT v2 | ParsBERT v1 | mBERT |
|:-----------------:|:-----------:|:-----------:|:-----:|
|    Persian News   |    97.44*   |    97.19    | 95.79 |


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