---
language: 
  - en
tags:
- biomedical
- bioNLP
---

This is a version of [PubmedBERT](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext?text=%5BMASK%5D+is+a+tumor+suppressor+gene.) which has been domain-adapted (via additional pretraining) to a set of PubMed abstracts that likely discuss multiple-drug therapies. This model was the strongest contextualized encoder in the experiments in the paper ["A Dataset for N-ary Relation Extraction of Drug Combinations"](https://arxiv.org/abs/2205.02289), when used as a component of a larger relation classification model (also hosted [here on Huggingface](https://huggingface.co/allenai/drug-combo-classifier-pubmedbert-dapt)).

If you use this model, cite both
```latex
@misc{pubmedbert,
  author = {Yu Gu and Robert Tinn and Hao Cheng and Michael Lucas and Naoto Usuyama and Xiaodong Liu and Tristan Naumann and Jianfeng Gao and Hoifung Poon},
  title = {Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing},
  year = {2020},
  eprint = {arXiv:2007.15779},
}
```

and

```latex
@inproceedings{Tiktinsky2022ADF,
    title = "A Dataset for N-ary Relation Extraction of Drug Combinations",
    author = "Tiktinsky, Aryeh and Viswanathan, Vijay and Niezni, Danna and Meron Azagury, Dana and Shamay, Yosi and Taub-Tabib, Hillel and Hope, Tom and Goldberg, Yoav",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.naacl-main.233",
    doi = "10.18653/v1/2022.naacl-main.233",
    pages = "3190--3203",
}
```