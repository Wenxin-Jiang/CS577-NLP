# Punctuator for Simplified Chinese

The model is fine-tuned based on `DistilBertForTokenClassification` for adding punctuations to plain text (simplified Chinese). The model is fine-tuned based on distilled model `bert-base-chinese`.

## Usage

```python
from transformers import DistilBertForTokenClassification, DistilBertTokenizerFast

model = DistilBertForTokenClassification.from_pretrained("Qishuai/distilbert_punctuator_zh")
tokenizer = DistilBertTokenizerFast.from_pretrained("Qishuai/distilbert_punctuator_zh")
```

## Model Overview

### Training data
Combination of following three dataset:

- News articles of People's Daily 2014. [Reference](https://github.com/InsaneLife/ChineseNLPCorpus)

### Model Performance
- Validation with MSRA training dataset. [Reference](https://github.com/InsaneLife/ChineseNLPCorpus/tree/master/NER/MSRA)
- Metrics Report:
    |                  | precision | recall | f1-score | support |
    |:----------------:|:---------:|:------:|:--------:|:-------:|
    |      C_COMMA     |    0.67   |  0.59  |   0.63   |  91566  |
    |     C_DUNHAO     |    0.50   |  0.37  |   0.42   |  21013  |
    | C_EXLAMATIONMARK |    0.23   |  0.06  |   0.09   |   399   |
    |     C_PERIOD     |    0.84   |  0.99  |   0.91   |  44258  |
    |  C_QUESTIONMARK  |    0.00   |  1.00  |   0.00   |    0    |
    |     micro avg    |    0.71   |  0.67  |   0.69   |  157236 |
    |     macro avg    |    0.45   |  0.60  |   0.41   |  157236 |
    |   weighted avg   |    0.69   |  0.67  |   0.68   |  157236 |


