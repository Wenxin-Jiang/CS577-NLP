---
metrics:
- accuracy
widget:
- text: "In war resolution, in defeat defiance, in victory magnanimity"
- text: "en la guerra resolución en la derrota desafío en la victoria magnanimidad"
---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dqeUwS_DZ-urrmYzB29nTCBUltwJxhbh?usp=sharing)

# 22 Language Identifier - BERT

This model is trained to identify the following 22 different languages. 


- Arabic 
- Chinese 
- Dutch 
- English 
- Estonian 
- French
- Hindi
- Indonesian 
- Japanese 
- Korean 
- Latin 
- Persian 
- Portugese 
- Pushto
- Romanian 
- Russian 
- Spanish 
- Swedish 
- Tamil 
- Thai 
- Turkish
- Urdu

## Loading the model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("SharanSMenon/22-languages-bert-base-cased")

model = AutoModelForSequenceClassification.from_pretrained("SharanSMenon/22-languages-bert-base-cased")
```

## Inference

```python
def predict(sentence):
  tokenized = tokenizer(sentence, return_tensors="pt")
  outputs = model(**tokenized)
  return model.config.id2label[outputs.logits.argmax(dim=1).item()]
```

### Examples

```python
sentence1 = "in war resolution, in defeat defiance, in victory magnanimity"
predict(sentence1) # English

sentence2 = "en la guerra resolución en la derrota desafío en la victoria magnanimidad"
predict(sentence2) # Spanish

sentence3 = "هذا هو أعظم إله على الإطلاق"
predict(sentence3) # Arabic
```