---
language: en
tags:
  - financial
  - stocks
  - topic
datasets:
- Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75
widget:
- text: "LexaGene Receives Signed Quote from Large Biopharma Company to Purchase a MiQLab System --  LexaGene Holdings, Inc., (OTCQB: LXXGF; TSX-V: LXG) (“LexaGene” or the “Company”), an innovative, molecular diagnostics company that has commercialized the MiQLab® System for automated, genetic testing, is pleased to announce that it has received an indication that a major biopharma company intends to purchase its technology."
- text: "Melcor REIT (TSX: MR.UN) today announced results for the third quarter ended September 30, 2022. Revenue was stable in the quarter and year-to-date. Net operating income was down 3% in the quarter at $11.61 million due to the timing of operating expenses and inflated costs including utilities like gas/heat and power"
- text: "Badger Infrastructure Solutions Ltd. Announces Resignation of Chief Financial Officer and Appointment of Interim Chief Financial Officer --  Badger Infrastructure Solutions Ltd. (“Badger” or the “Company”) (TSX:BDGI) announced today the resignation of Mr. Darren Yaworsky, Senior Vice President, Finance & Chief Financial Officer and the appointment of Mr. Pramod Bhatia as interim Chief Financial Officer. Mr. Yaworsky will remain with the Company until December 31, 2022 to facilitate an orderly transition."
license: mit
---

# Model fine-tuned from roberta-large for topic classification of financial news (emphasis on Canadian news).

### Introduction
This model was train on the topic column of financial_news_sentiment_mixte_with_phrasebank_75 dataset.
The topic column was generated using a zero-shot classification model on 11 topics. 
There was no manual reviews on the generated topics and therefore we should expect misclassifications in the dataset, 
and therefore the trained model might reproduce the same errors.


### Training data
Training data was classified as follow:

class |Description
-|-
0 |acquisition
1 |other
2 |quaterly financial release
3 |appointment to new position
4 |dividend
5 |corporate update
6 |drillings results
7 |conference
8 |share repurchase program
9 |grant of stocks


### How to use roberta-large-financial-news-topics-en with HuggingFace

##### Load roberta-large-financial-news-topics-en and its sub-word tokenizer :

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-large-financial-news-topics-en")
model = AutoModelForSequenceClassification.from_pretrained("Jean-Baptiste/roberta-large-financial-news-topics-en")


##### Process text sample (from wikipedia)

from transformers import pipeline

pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)
pipe("Melcor REIT (TSX: MR.UN) today announced results for the third quarter ended September 30, 2022. Revenue was stable in the quarter and year-to-date. Net operating income was down 3% in the quarter at $11.61 million due to the timing of operating expenses and inflated costs including utilities like gas/heat and power")

[{'label': 'quaterly financial release', 'score': 0.8829097151756287}]

```

### Model performances

Overall f1 score (average macro)

precision|recall|f1
-|-|-
0.7533|0.7629|0.7499


