---
language: de
tags:
- bert
license: apache-2.0

widget:
- text: "Das Frühstück ist sehr gut, es gibt auch Laktosefreie Produkte."
  example_title: "Example 1"
- text: "Das Personal ist sehr kompetent und sehr freundlich."
  example_title: "Example 2"
- text: "Die Zimmer sind wie beschrieben sehr klein, vergleichbar mit einer Kreuzfahrtschiffkabine. "
  example_title: "Example 3"
- text: "Scheinwerfer vor dem Zimmer ganze Nacht an und zu hell"
  example_title: "Example 4"
---

# German Hotel Review Sentiment Classification
A model trained on German Hotel Reviews from Switzerland. The base model is the [bert-base-german-cased](https://huggingface.co/bert-base-german-cased). The last hidden layer of the base model was extracted and a classification layer was added. The entire model was then trained for 5 epochs on our dataset.

# Model Performance

| Classes | Precision | Recall | F1 Score |
| :---: | :---: | :---: |:---: |
| Positive | 90.48% | 82.61% | 86.36% |
| Negative | 70.59% | 92.31% | 80.00% |
| Neutral | 28.57% | 13.33% | 18.18% |
| Accuracy |  |  | 76.00% |
| Macro Average | 63.21% | 62.75% | 61.52% |
| Weighted Average | 73.43% | 76.00% | 73.65% |

## Confusion Matrix
![Confusion Matrix](bert-base-german-cased_German_sentiment.jpg)