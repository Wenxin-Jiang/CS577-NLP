---
language: "en"

tags:
- English
- Bible

dataset:
- English Bible Translation Dataset
- Link: https://www.kaggle.com/oswinrh/bible

inference: false

---

## Dataset 

English Bible Translation Dataset (https://www.kaggle.com/oswinrh/bible)

*NOTE:* It is `roberta-base` fine-tuned (for MLM objective) for 1 epoch (using MLM objective) on the 7 `.csv` files mentioned above, which consist of around 5.5M words.

## Citation

If you use this model in your work, please add the following citation -
```
@inproceedings{nandy-etal-2021-cs60075,
    title = "cs60075{\_}team2 at {S}em{E}val-2021 Task 1 : Lexical Complexity Prediction using Transformer-based Language Models pre-trained on various text corpora",
    author = "Nandy, Abhilash  and
      Adak, Sayantan  and
      Halder, Tanurima  and
      Pokala, Sai Mahesh",
    booktitle = "Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.semeval-1.87",
    doi = "10.18653/v1/2021.semeval-1.87",
    pages = "678--682",
    abstract = "The main contribution of this paper is to fine-tune transformer-based language models pre-trained on several text corpora, some being general (E.g., Wikipedia, BooksCorpus), some being the corpora from which the CompLex Dataset was extracted, and others being from other specific domains such as Finance, Law, etc. We perform ablation studies on selecting the transformer models and how their individual complexity scores are aggregated to get the resulting complexity scores. Our method achieves a best Pearson Correlation of 0.784 in sub-task 1 (single word) and 0.836 in sub-task 2 (multiple word expressions).",
}
```
