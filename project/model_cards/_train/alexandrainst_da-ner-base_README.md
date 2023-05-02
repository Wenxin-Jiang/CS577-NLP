---
language:
- da
license: cc-by-sa-4.0
datasets:
- dane
widget:
- text: "Jens Peter Hansen kommer fra Danmark"
---

# BERT fine-tuned for Named Entity Recognition in Danish

The model tags tokens (in Danish sentences) with named entity tags (BIO format) [PER, ORG, LOC, MISC].
The pretrained language model used for fine-tuning is the [Danish BERT](https://github.com/certainlyio/nordic_bert) by BotXO. 

See the [DaNLP documentation](https://danlp-alexandra.readthedocs.io/en/latest/docs/tasks/ner.html#bert) for more details.

Here is how to use the model:

```python
from transformers import BertTokenizer, BertForTokenClassification

model = BertForTokenClassification.from_pretrained("alexandrainst/da-ner-base")
tokenizer = BertTokenizer.from_pretrained("alexandrainst/da-ner-base")
```

## Training Data 

The model has been trained on the [DaNE](https://danlp-alexandra.readthedocs.io/en/latest/docs/datasets.html#dane). 