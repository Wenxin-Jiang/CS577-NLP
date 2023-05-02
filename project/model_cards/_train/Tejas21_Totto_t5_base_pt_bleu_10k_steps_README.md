---
license: apache-2.0
---
language: 
- en

tags:
- Table to text
- Data to text

## Dataset:
- [ToTTo](https://github.com/google-research-datasets/ToTTo)
A Controlled Table-to-Text Dataset. Totto is an open-source table-to-text dataset with over 1,20,000 examples in the English language. It defines a controlled generation task as: given a Wikipedia table and a set of highlighted cells, generate a one-sentence description.

## Base Model - T5-Base
[Google's T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) 
The T5 was built by the Google team in order to create a general-purpose model that can understand the text. The basic idea behind t5 was to deal with the text processing problem as a “text-to-text” problem, i.e. taking the text as input and producing new text as output.

## Baseline Preprocessing
[Baseline Preprocessing](https://github.com/google-research/language/tree/master/language/totto)
This code repository serves as a supplementary for the main repository, which can be used to do basic preprocessing of the Totto dataset.
 
## Fine-tuning
We used the T5 for the conditional generation model to fine-tune with, 10000 steps with the ToTTo dataset using BLEU as a metric.


