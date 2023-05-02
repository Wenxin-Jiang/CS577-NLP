---
language: ml
license: apache-2.0
---
This model is used to detect **Offensive Content** in **Malayalam Code-Mixed language**. The mono in the name refers to the monolingual setting, where the model is trained using only Malayalam(pure and code-mixed) data. The weights are initialized from pretrained XLM-Roberta-Base and pretrained using Masked Language Modelling on the target dataset before fine-tuning using Cross-Entropy Loss.

This model is the best of multiple trained for **EACL 2021 Shared Task on Offensive Language Identification in Dravidian Languages**. Genetic-Algorithm based ensembled test predictions got the highest weighted F1 score at the leaderboard (Weighted F1 score on hold out test set: This model - 0.97, Ensemble - 0.97)

### For more details about our paper

Debjoy Saha, Naman Paharia, Debajit Chakraborty, Punyajoy Saha, Animesh Mukherjee. "[Hate-Alert@DravidianLangTech-EACL2021: Ensembling strategies for Transformer-based Offensive language Detection](https://www.aclweb.org/anthology/2021.dravidianlangtech-1.38/)".

***Please cite our paper in any published work that uses any of these resources.***
~~~
@inproceedings{saha-etal-2021-hate,
    title = "Hate-Alert@{D}ravidian{L}ang{T}ech-{EACL}2021: Ensembling strategies for Transformer-based Offensive language Detection",
    author = "Saha, Debjoy and Paharia, Naman and Chakraborty, Debajit and Saha, Punyajoy and Mukherjee, Animesh",
    booktitle = "Proceedings of the First Workshop on Speech and Language Technologies for Dravidian Languages",
    month = apr,
    year = "2021",
    address = "Kyiv",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.dravidianlangtech-1.38",
    pages = "270--276",
    abstract = "Social media often acts as breeding grounds for different forms of offensive content. For low resource languages like Tamil, the situation is more complex due to the poor performance of multilingual or language-specific models and lack of proper benchmark datasets. Based on this shared task {``}Offensive Language Identification in Dravidian Languages{''} at EACL 2021; we present an exhaustive exploration of different transformer models, We also provide a genetic algorithm technique for ensembling different models. Our ensembled models trained separately for each language secured the first position in Tamil, the second position in Kannada, and the first position in Malayalam sub-tasks. The models and codes are provided.",
}
~~~