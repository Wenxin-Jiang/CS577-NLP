---
language:
- da
license: cc-by-sa-4.0
widget:
- text: Der er et træ i haven.
---

# Danish BERT for emotion detection

The BERT Emotion model detects whether a Danish text is emotional or not. 
It is based on the pretrained [Danish BERT](https://github.com/certainlyio/nordic_bert) model by BotXO which has been fine-tuned on social media data. 

See the [DaNLP documentation](https://danlp-alexandra.readthedocs.io/en/latest/docs/tasks/sentiment_analysis.html#bert-emotion) for more details. 


Here is how to use the model:

```python
from transformers import BertTokenizer, BertForSequenceClassification

model = BertForSequenceClassification.from_pretrained("alexandrainst/da-binary-emotion-classification-base")
tokenizer = BertTokenizer.from_pretrained("alexandrainst/da-binary-emotion-classification-base")
```

## Training data

The data used for training has not been made publicly available. It consists of social media data manually annotated in collaboration with Danmarks Radio.

