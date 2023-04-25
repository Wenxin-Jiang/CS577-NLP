---
tags: 
- question-answering
datasets:
- squad
- anukaver/EstQA
---

# Question answering model for Estonian
This is a question answering model based on XLM-Roberta base model. It is fine-tuned subsequentially on:
1. English SQuAD v1.1
2. SQuAD v1.1 translated into Estonian
3. Small native Estonian dataset (800 samples)

The model has retained good multilingual properties and can be used for extractive QA tasks in all languages included in XLM-Roberta. The performance is best in the fine-tuning languages of Estonian and English.

| Tested on | F1 | EM |
| ----------- | --- | --- |
| EstQA test set | 82.4 | 75.3 |
| SQuAD v1.1 dev set | 86.9 | 77.9 |

The Estonian dataset used for fine-tuning and validating results is available in https://huggingface.co/datasets/anukaver/EstQA/ (version 1.0)