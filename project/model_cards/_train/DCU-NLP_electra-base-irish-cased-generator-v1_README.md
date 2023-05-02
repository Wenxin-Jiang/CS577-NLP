---
language:
- ga
license: apache-2.0
tags:
- irish
- electra
widget:
- text: "Ceoltóir [MASK] ab ea Johnny Cash."
---

# gaELECTRA
[gaELECTRA](https://aclanthology.org/2022.lrec-1.511/) is an ELECTRA model trained on 7.9M Irish sentences. For more details, including the hyperparameters and pretraining corpora used please refer to our paper. For fine-tuning this model on a token classification task, e.g. Named Entity Recognition, use the discriminator model.

### Limitations and bias
Some data used to pretrain gaBERT was scraped from the web which potentially contains ethically problematic text (bias, hate, adult content, etc.). Consequently, downstream tasks/applications using gaBERT should be thoroughly tested with respect to ethical considerations.


### BibTeX entry and citation info
If you use this model in your research, please consider citing our paper:

```
@inproceedings{barry-etal-2022-gabert,
    title = "ga{BERT} {---} an {I}rish Language Model",
    author = "Barry, James  and
      Wagner, Joachim  and
      Cassidy, Lauren  and
      Cowap, Alan  and
      Lynn, Teresa  and
      Walsh, Abigail  and
      {\'O} Meachair, M{\'\i}che{\'a}l J.  and
      Foster, Jennifer",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.511",
    pages = "4774--4788",
    abstract = "The BERT family of neural language models have become highly popular due to their ability to provide sequences of text with rich context-sensitive token encodings which are able to generalise well to many NLP tasks. We introduce gaBERT, a monolingual BERT model for the Irish language. We compare our gaBERT model to multilingual BERT and the monolingual Irish WikiBERT, and we show that gaBERT provides better representations for a downstream parsing task. We also show how different filtering criteria, vocabulary size and the choice of subword tokenisation model affect downstream performance. We compare the results of fine-tuning a gaBERT model with an mBERT model for the task of identifying verbal multiword expressions, and show that the fine-tuned gaBERT model also performs better at this task. We release gaBERT and related code to the community.",
}
```