---
language:
- es

widget:
- text: "MMG se dedica a la <mask> artificial."

---

# mlm-spanish-roberta-base

This model has a RoBERTa base architecture and was trained from scratch with 3.6 GB of raw text over 10 epochs. 4 Tesla V-100 GPUs were used for the training.

To test the quality of the resulting model we evaluate it over the [GLUES](https://github.com/dccuchile/GLUES) benchmark for Spanish NLU. The results are the following:

|          Task           |     Score (metric)    |
|:-----------------------:|:---------------------:|
|           XNLI          |    71.99 (accuracy)   |
|       Paraphrasing      |    74.85 (accuracy)   |
|           NER           |       85.34 (F1)      |
|           POS           |    97.49 (accuracy)   |
|    Dependency Parsing   | 85.14/81.08 (UAS/LAS) |
| Document Classification |    93.00 (accuracy)   |
