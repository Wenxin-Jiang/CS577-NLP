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
| :--- | :---: | :---: |:---: |
| Room | 84.62% | 88.00% | 86.27% |
| Food | 79.17% | 82.61% | 80.85% |
| Staff | 63.64% | 70.00% | 66.67% |
| Location | 83.33% | 62.50% | 71.43% |
| GeneralUtilitys | 76.92% | 76.92% | 76.92% |
| HotelOrganisation | 26.67% | 30.77% | 28.57% |
| Unknown | 25.00% | 16.67% | 20.00% |
| ReasonForStay | 100.00% | 50.00% | 66.67% |
| Accuracy |  |  | 69.00% |
| Macro Average | 67.42% | 59.68% | 62.17% |
| Weighted Average | 69.36% | 69.00% | 68.79% |

## Confusion Matrix
![Confusion Matrix](bert-base-german-cased_German_classification.jpg)
