---
language:
- da
license: cc-by-sa-4.0
datasets:
- DDSC/twitter-sent
- DDSC/europarl
widget:
- text: Jeg tror alligvel, det bliver godt
---

# Danish BERT Tone for the detection of subjectivity/objectivity

The BERT Tone model detects whether a text (in Danish) is subjective or objective. 
The model is based on the finetuning of the pretrained [Danish BERT](https://github.com/certainlyio/nordic_bert) model by BotXO. 

See the [DaNLP documentation](https://danlp-alexandra.readthedocs.io/en/latest/docs/tasks/sentiment_analysis.html#bert-tone) for more details. 


Here is how to use the model:

```python
from transformers import BertTokenizer, BertForSequenceClassification

model = BertForSequenceClassification.from_pretrained("alexandrainst/da-subjectivivity-classification-base")
tokenizer = BertTokenizer.from_pretrained("alexandrainst/da-subjectivivity-classification-base")
```

## Training data

The data used for training come from the [Twitter Sentiment](https://danlp-alexandra.readthedocs.io/en/latest/docs/datasets.html#twitsent) and [EuroParl sentiment 2](https://danlp-alexandra.readthedocs.io/en/latest/docs/datasets.html#europarl-sentiment2) datasets.