---
tags:
- flair
- token-classification
- sequence-tagger-model
language: fa
dataset:
-  NSURL-2019
widget:
- text: "آخرین مقام برجسته ژاپنی که پس از انقلاب 57  تاکنون به ایران سفر کرده است شینتارو آبه است."
---

## Persian NER in Flair

This is the universal Named-entity recognition model for Persian that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **84.03** (NSURL-2019)

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

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("hamedkhaledi/persain-flair-ner")

# make example sentence
sentence = Sentence("آخرین مقام برجسته ژاپنی که پس از انقلاب 57  تاکنون به ایران سفر کرده است شینتارو آبه است.")

tagger.predict(sentence)
#print result
print(sentence.to_tagged_string())
```

This yields the following output:
```
آخرین مقام برجسته ژاپنی که پس از انقلاب 57 <B-DAT> تاکنون به ایران <B-LOC> سفر کرده است شینتارو <B-PER> آبه <I-PER> است .
```

---

### Results
- F-score (micro) 0.8403
- F-score (macro) 0.8656
- Accuracy 0.7357

```
By class:
              precision    recall  f1-score   support

         LOC     0.8789    0.8589    0.8688      4083
         ORG     0.8390    0.7653    0.8005      3166
         PER     0.8395    0.8169    0.8280      2741
         DAT     0.8648    0.7957    0.8288      1150
         MON     0.9758    0.9020    0.9374       357
         TIM     0.8500    0.8193    0.8344       166
         PCT     0.9615    0.9615    0.9615       156

   micro avg     0.8616    0.8200    0.8403     11819
   macro avg     0.8871    0.8456    0.8656     11819
weighted avg     0.8613    0.8200    0.8400     11819
 samples avg     0.7357    0.7357    0.7357     11819

Loss: 0.06893542408943176'

```