---
language:
- en

---

# FS-distilroberta-fine-tuned

The model was obtained by fine-tuning "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis" model for sentiment analysis on financial news gathered by FinScience software. It predicts the sentiment of news with one label ("negative", "neutral" or "positive"). At the moment, the models works only in English.


## Training data

The training dataset consists of 2558 titles of news that were manually labelled by FinScience Team using doccano tool. A "neutral" label was assigned to those news for which an agreement was not reached. 70% (1790 news) of such dataset was employed as training set, while 15% (384) as validation set and the remaining 15% as test set. F1-score (macro) was selected as the evaluation metric.

| Set | Number of news |  Scope |
| -------- | ----------------- | ----------------- |
| Training  | 1790           | Training the model|
| Validation    | 384            | Selecting the hyper-parameters  |
| Test   | 384           | Evaluating the performance|


## Accuracy

The table below summarizes the performance of the models that were tested on the same test set, consisting of 384 held-out titles:


| Language | Accuracy| F1-score (macro) |
| -------- | ---------------------- | ------------------- |
| FS-distilroberta-fine-tuned  | 76%| 76%
