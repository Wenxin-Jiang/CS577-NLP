# Punctuator for Uncased English

The model is fine-tuned based on `DistilBertForTokenClassification` for adding punctuations to plain text (uncased English)

## Usage

```python
from transformers import DistilBertForTokenClassification, DistilBertTokenizerFast

model = DistilBertForTokenClassification.from_pretrained("Qishuai/distilbert_punctuator_en")
tokenizer = DistilBertTokenizerFast.from_pretrained("Qishuai/distilbert_punctuator_en")
```

## Model Overview

### Training data
Combination of following three dataset:

- BBC news: From BBC news website corresponding to stories in five topical areas from 2004-2005. [Reference](https://www.kaggle.com/hgultekin/bbcnewsarchive)
- News articles: 20000 samples of short news articles scraped from Hindu, Indian times and Guardian between Feb 2017 and Aug 2017 [Reference](https://www.kaggle.com/sunnysai12345/news-summary?select=news_summary_more.csv)
- Ted talks: transcripts of over 4,000 TED talks between 2004 and 2019 [Reference](https://www.kaggle.com/miguelcorraljr/ted-ultimate-dataset)

### Model Performance
- Validation with 500 samples of dataset scraped from https://www.thenews.com.pk website. [Reference](https://www.kaggle.com/asad1m9a9h6mood/news-articles)
- Metrics Report:

    |                | precision | recall | f1-score | support |
    |:--------------:|:---------:|:------:|:--------:|:-------:|
    |      COMMA     |    0.66   |  0.55  |   0.60   |   7064  |
    | EXLAMATIONMARK |    1.00   |  0.00  |   0.00   |    5    |
    |     PERIOD     |    0.73   |  0.63  |   0.68   |   6573  |
    |  QUESTIONMARK  |    0.54   |  0.41  |   0.47   |    17   |
    |    micro avg   |    0.69   |  0.59  |   0.64   |  13659  |
    |    macro avg   |    0.73   |  0.40  |   0.44   |  13659  |
    |  weighted avg  |    0.69   |  0.59  |   0.64   |  13659  |


- Validation with 86 news ted talks of 2020 which are not included in training dataset [Reference](https://www.kaggle.com/thegupta/ted-talk)
- Metrics Report:
    |                | precision | recall | f1-score | support |
    |:--------------:|:---------:|:------:|:--------:|:-------:|
    |      COMMA     |    0.71   |  0.56  |   0.63   |  10712  |
    | EXLAMATIONMARK |    0.45   |  0.07  |   0.12   |    75   |
    |     PERIOD     |    0.75   |  0.65  |   0.70   |   7921  |
    |  QUESTIONMARK  |    0.73   |  0.67  |   0.70   |   827   |
    |    micro avg   |    0.73   |  0.60  |   0.66   |  19535  |
    |    macro avg   |    0.66   |  0.49  |   0.53   |  19535  |
    |  weighted avg  |    0.73   |  0.60  |   0.66   |  19535  |


