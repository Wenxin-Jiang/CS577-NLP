---
language: en
tags:
- financial-sentiment-analysis
- sentiment-analysis
datasets:
- financial_phrasebank
widget:
- text: Operating profit rose to EUR 13.1 mn from EUR 8.7 mn in the corresponding period in 2007 representing 7.7 % of net sales.
- text: Bids or offers include at least 1,000 shares and the value of the shares must correspond to at least EUR 4,000.
- text: Raute reported a loss per share of EUR 0.86 for the first half of 2009 , against EPS of EUR 0.74 in the corresponding period of 2008.
---
### FinancialBERT for Sentiment Analysis

[*FinancialBERT*](https://huggingface.co/ahmedrachid/FinancialBERT) is a BERT model pre-trained on a large corpora of financial texts. The purpose is to enhance financial NLP research and practice in financial domain, hoping that financial practitioners and researchers can benefit from this model without the necessity of the significant computational resources required to train the model. 

The model was fine-tuned for Sentiment Analysis task on _Financial PhraseBank_ dataset. Experiments show that this model outperforms the general BERT and other financial domain-specific models.
 
More details on `FinancialBERT`'s pre-training process can be found at: https://www.researchgate.net/publication/358284785_FinancialBERT_-_A_Pretrained_Language_Model_for_Financial_Text_Mining

### Training data
FinancialBERT model was fine-tuned on [Financial PhraseBank](https://www.researchgate.net/publication/251231364_FinancialPhraseBank-v10), a dataset consisting of 4840 Financial News categorised by sentiment (negative, neutral, positive).

### Fine-tuning hyper-parameters
- learning_rate = 2e-5
- batch_size = 32
- max_seq_length = 512
- num_train_epochs = 5

### Evaluation metrics
The evaluation metrics used are: Precision, Recall and F1-score. The following is the classification report on the test set.

| sentiment  | precision        | recall           | f1-score  | support  |
| ------------- |:-------------:|:-------------:|:-------------:| -----:|
| negative | 0.96      | 0.97 | 0.97 | 58 |
| neutral | 0.98      | 0.99 | 0.98 | 279 |
| positive | 0.98     | 0.97 | 0.97 | 148 |
| macro avg | 0.97     | 0.98 | 0.98 | 485 |
| weighted avg | 0.98     | 0.98 | 0.98 | 485 |

 ### How to use 
The model can be used thanks to Transformers pipeline for sentiment analysis.
```python
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

model = BertForSequenceClassification.from_pretrained("ahmedrachid/FinancialBERT-Sentiment-Analysis",num_labels=3)
tokenizer = BertTokenizer.from_pretrained("ahmedrachid/FinancialBERT-Sentiment-Analysis")

nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

sentences = ["Operating profit rose to EUR 13.1 mn from EUR 8.7 mn in the corresponding period in 2007 representing 7.7 % of net sales.",  
             "Bids or offers include at least 1,000 shares and the value of the shares must correspond to at least EUR 4,000.", 
             "Raute reported a loss per share of EUR 0.86 for the first half of 2009 , against EPS of EUR 0.74 in the corresponding period of 2008.", 
             ]
results = nlp(sentences)
print(results)

[{'label': 'positive', 'score': 0.9998133778572083},
 {'label': 'neutral', 'score': 0.9997822642326355},
 {'label': 'negative', 'score': 0.9877365231513977}]
```

> Created by [Ahmed Rachid Hazourli](https://www.linkedin.com/in/ahmed-rachid/)
