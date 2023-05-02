---
language:
- da
license: cc-by-sa-4.0
widget:
- text: Jeg ejer en rød bil og det er en god bil.
---

# Danish BERT for emotion classification

The BERT Emotion model classifies a Danish text in one of the following class:
* Glæde/Sindsro
* Tillid/Accept
* Forventning/Interrese
* Overasket/Målløs
* Vrede/Irritation
* Foragt/Modvilje
* Sorg/trist
* Frygt/Bekymret

It is based on the pretrained [Danish BERT](https://github.com/certainlyio/nordic_bert) model by BotXO which has been fine-tuned on social media data. 

This model should be used after detecting whether the text contains emotion or not, using the binary [BERT Emotion model](https://huggingface.co/alexandrainst/da-binary-emotion-classification-base).

See the [DaNLP documentation](https://danlp-alexandra.readthedocs.io/en/latest/docs/tasks/sentiment_analysis.html#bert-emotion) for more details. 

Here is how to use the model:

```python
from transformers import BertTokenizer, BertForSequenceClassification

model = BertForSequenceClassification.from_pretrained("alexandrainst/da-emotion-classification-base")
tokenizer = BertTokenizer.from_pretrained("alexandrainst/da-emotion-classification-base")
```

## Training data

The data used for training has not been made publicly available. It consists of social media data manually annotated in collaboration with Danmarks Radio.

