---
language: en
tags:
  - financial
  - stocks
  - sentiment
datasets:
- Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75
widget:
- text: "Fortuna Silver Mines Inc. (NYSE: FSM) (TSX: FVI) reports solid production results for the third quarter of 2022 from its four operating mines in the Americas and West Africa."
- text: "Theratechnologies Reports Financial Results for the Third Quarter of Fiscal 2022 and Provides Business Update -- - Q3 2022 Consolidated Revenue Growth of 17% to $20.8 million"
- text: "The Flowr Corporation To File for CCAA Protection"
- text: "Melcor REIT (TSX: MR.UN) today announced results for the third quarter ended September 30, 2022. Revenue was stable in the quarter and year-to-date. Net operating income was down 3% in the quarter at $11.61 million due to the timing of operating expenses and inflated costs including utilities like gas/heat and power"

license: mit
---

# Model fine-tuned from roberta-large for sentiment classification of financial news (emphasis on Canadian news).

### Introduction
This model was train on financial_news_sentiment_mixte_with_phrasebank_75 dataset.
This is a customized version of the phrasebank dataset in which I kept only sentence validated by at least 75% annotators. 
In addition I added ~2000 articles validated manually on Canadian financial news. Therefore the model is more specifically trained for Canadian news.
Final result is f1 score of 93.25% overall and 83.6% on Canadian news.




### Training data
Training data was classified as follow:

class |Description
-|-
0 |negative
1 |neutral
2 |positive


### How to use roberta-large-financial-news-sentiment-en with HuggingFace

##### Load roberta-large-financial-news-sentiment-en and its sub-word tokenizer :

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-large-financial-news-sentiment-en")
model = AutoModelForSequenceClassification.from_pretrained("Jean-Baptiste/roberta-large-financial-news-sentiment-en")


##### Process text sample (from wikipedia)

from transformers import pipeline

pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)
pipe("Melcor REIT (TSX: MR.UN) today announced results for the third quarter ended September 30, 2022. Revenue was stable in the quarter and year-to-date. Net operating income was down 3% in the quarter at $11.61 million due to the timing of operating expenses and inflated costs including utilities like gas/heat and power")

[{'label': 'negative', 'score': 0.9399105906486511}]

```

### Model performances

Overall f1 score (average macro)

precision|recall|f1
-|-|-
0.9355|0.9299|0.9325

By entity

entity|precision|recall|f1
-|-|-|-
negative|0.9605|0.9240|0.9419 
neutral|0.9538|0.9459|0.9498
positive|0.8922|0.9200|0.9059
