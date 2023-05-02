---
language:
- en
license: gpl-3.0
tags:
- misogyny detection
- abusive language
- hate speech
- offensive language
widget:
- text: I believe religious minorities need to be protected more.
  example_title: Hate Speech Detection Example 1
pipeline_tag: text-classification
datasets:
- nedjmaou/MLMA_hate_speech
---

# Entropy-based Attention Regularization 👂

This is an English BERT fine-tuned with [Entropy-based Attention Regularization](https://aclanthology.org/2022.findings-acl.88/) to reduce lexical overfitting to specific words on the task of Misogyny Identification.
Use this model if you want a debiased alternative to a BERT classifier.

Please refer to the paper to know all the training details.

## Dataset

The model was fine-tuned on the English part of the [MLMA dataset](https://aclanthology.org/D19-1474/).

## Model

This model is the fine-tuned version of the [bert-base-uncased](https://huggingface.co/bert-base-uncased) model.
We trained a total of three versions for Italian and English. 

| Model                       | Download |
| ------                      | -------------------------|
| `bert-base-uncased-ear-misogyny` | [Link](https://huggingface.co/MilaNLProc/bert-base-uncased-ear-misogyny) |
| `bert-base-uncased-ear-mlma` | [Link](https://huggingface.co/MilaNLProc/bert-base-uncased-ear-mlma) |
| `bert-base-uncased-ear-misogyny-italian`   | [Link](https://huggingface.co/MilaNLProc/bert-base-uncased-ear-misogyny-italian) |

# Authors
- [Giuseppe Attanasio](https://gattanasio.cc/)
- [Debora Nozza](http://dnozza.github.io/)
- [Dirk Hovy](https://federicobianchi.io/)
- [Elena Baralis](https://dbdmg.polito.it/wordpress/people/elena-baralis/)

# Citation

Please use the following BibTeX entry if you use this model in your project:

```
@inproceedings{attanasio-etal-2022-entropy,
    title = "Entropy-based Attention Regularization Frees Unintended Bias Mitigation from Lists",
    author = "Attanasio, Giuseppe  and
      Nozza, Debora  and
      Hovy, Dirk  and
      Baralis, Elena",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2022",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-acl.88",
    doi = "10.18653/v1/2022.findings-acl.88",
    pages = "1105--1119",
    abstract = "Natural Language Processing (NLP) models risk overfitting to specific terms in the training data, thereby reducing their performance, fairness, and generalizability. E.g., neural hate speech detection models are strongly influenced by identity terms like gay, or women, resulting in false positives, severe unintended bias, and lower performance.Most mitigation techniques use lists of identity terms or samples from the target domain during training. However, this approach requires a-priori knowledge and introduces further bias if important terms are neglected.Instead, we propose a knowledge-free Entropy-based Attention Regularization (EAR) to discourage overfitting to training-specific terms. An additional objective function penalizes tokens with low self-attention entropy.We fine-tune BERT via EAR: the resulting model matches or exceeds state-of-the-art performance for hate speech classification and bias metrics on three benchmark corpora in English and Italian.EAR also reveals overfitting terms, i.e., terms most likely to induce bias, to help identify their effect on the model, task, and predictions.",
}
```

# Limitations

Entropy-Attention Regularization mitigates lexical overfitting but does not completely remove it. We expect the model still to show biases, e.g., peculiar keywords that induce a specific prediction regardless of the context.

Please refer to our paper for a quantitative evaluation of this mitigation. 

# License 
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)