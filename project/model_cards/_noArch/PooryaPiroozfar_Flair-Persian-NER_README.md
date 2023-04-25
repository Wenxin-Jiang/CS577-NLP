---
tags:
- flair
- token-classification
- sequence-tagger-model
language: fa
dataset:
- NSURL-2019
widget:
- text: >-
    اولین نمایش این فیلم‌ها روز دوشنبه 13 اردیبهشت و از ساعت 21 در موزه سینماست.
metrics:
- f1
---

## Persian NER Using Flair

This is the 7-class Named-entity recognition model for Persian that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **90.33** (NSURL-2019)

Predicts NER tags:

| **tag**                        | **meaning** |
|:---------------------------------:|:-----------:|
| PER         | person name | 
| LOC         | location name | 
| ORG         | organization name | 
| DAT         | date |
| TIM         | time |
| PCT         | percent |
| MON         | Money|

Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and Pars-Bert.

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("PooryaPiroozfar/Flair-Persian-NER")

# make example sentence
sentence = Sentence("اولین نمایش این فیلم‌ها روز دوشنبه 13 اردیبهشت و از ساعت 21 در موزه سینماست.")

# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following NER tags are found:')
# iterate over entities and print
for entity in sentence.get_spans('ner'):
    print(entity)
```

This yields the following output:
```
Span[4:8]: "روز دوشنبه 13 اردیبهشت" → DAT (1.0)
Span[10:12]: "ساعت 21" → TIM (1.0)
Span[13:15]: "موزه سینماست" → LOC (0.9999)

```

---

### Results
- F-score (micro) 0.9033
- F-score (macro) 0.8976
- Accuracy 0.8277

```
By class:
              precision    recall  f1-score   support

         ORG     0.9016    0.8667    0.8838      1523
         LOC     0.9113    0.9305    0.9208      1425
         PER     0.9216    0.9322    0.9269      1224
         DAT     0.8623    0.7958    0.8277       480
         MON     0.9665    0.9558    0.9611       181
         PCT     0.9375    0.9740    0.9554        77
         TIM     0.8235    0.7925    0.8077        53

   micro avg     0.9081    0.8984    0.9033      4963
   macro avg     0.9035    0.8925    0.8976      4963
weighted avg     0.9076    0.8984    0.9028      4963
 samples avg     0.8277    0.8277    0.8277      4963
              
```