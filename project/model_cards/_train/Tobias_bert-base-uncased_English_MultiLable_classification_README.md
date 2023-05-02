---
language: eng
tags:
- bert
license: apache-2.0

widget:
- text: "The hotel is very nicely located"
  example_title: "Example 1"
- text: "The reception staff were extremely helpful and very welcoming"
  example_title: "Example 2"
- text: "There is no balcony in the rooms on the mountain side"
  example_title: "Example 3"
- text: "A bit pricey"
  example_title: "Example 4"
---

# English Hotel Review MultiLabel Classification
A model trained on English Hotel Reviews from Switzerland. The base model is the [bert-base-uncased](https://huggingface.co/bert-base-uncased). The last hidden layer of the base model was extracted and a classification layer was added. The entire model was then trained for 5 epochs on our dataset.

# Model Performance

| Classes | Precision | Recall | F1 Score |
| :--- | :---: | :---: |:---: |
| Room | 77.78% | 77.78% | 77.78% |
| Location | 95.45% | 95.45% | 95.45% |
| Staff | 75.00% | 93.75% | 83.33% |
| Unknown | 71.43% | 50.00% | 58.82% |
| HotelOrganisation | 27.27% | 30.00% | 28.57% |
| Food | 87.50% | 87.50% | 87.50% |
| ReasonForStay | 63.64% | 58.33% | 60.87%|
| GeneralUtility | 66.67% | 50.00% | 66.67% |
| Accuracy |  |  | 74.00% |
| Macro Average | 70.59%| 67.85% | 68.68% |
| Weighted Average | 74.17% | 74.00% | 73.66% |

## Confusion Matrix
![Confusion Matrix](bert-base-uncased_English_classification.jpg)