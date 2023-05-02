---
language:
- da
license: cc-by-4.0
widget:
- text: "Senile gamle idiot"
---

# Danish ELECTRA for hate speech (offensive language) detection

The ELECTRA Offensive model detects whether a Danish text is offensive or not. 
It is based on the pretrained [Danish Ælæctra](Maltehb/aelaectra-danish-electra-small-cased) model. 

See the [DaNLP documentation](https://danlp-alexandra.readthedocs.io/en/latest/docs/tasks/hatespeech.html#electra) for more details. 


Here is how to use the model:

```python
from transformers import ElectraTokenizer, ElectraForSequenceClassification

model = ElectraForSequenceClassification.from_pretrained("alexandrainst/da-hatespeech-detection-small")
tokenizer = ElectraTokenizer.from_pretrained("alexandrainst/da-hatespeech-detection-small")
```

## Training data

The data used for training has not been made publicly available. It consists of social media data manually annotated in collaboration with Danmarks Radio.

