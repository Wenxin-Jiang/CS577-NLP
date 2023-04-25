---
tags:
- flair
- token-classification
- sequence-tagger-model
language: 
-  fa
datasets:
- ontonotes
widget:
- text: "مقامات مصری به خاطر حفظ ثبات کشور در منطقهای پرآشوب بر خود میبالند ، در حالی که این کشور در طول ۱۶ سال گذشته تنها هشت سال آنرا بدون اعلام وضعیت اضطراری سپری کرده است ."
---

## Persian Universal Part-of-Speech Tagging in Flair

This is the universal part-of-speech tagging model for Persian that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **97,73** (UD_PERSIAN)

Predicts Universal POS tags:

| **tag**                        | **meaning** |
|:---------------------------------:|:-----------:|
|ADJ |  adjective |
|   ADP |  adposition |
|   ADV |  adverb |
|   AUX |  auxiliary |
|   CCONJ |  coordinating conjunction |
|   DET |  determiner |
|   INTJ |  interjection |
|   NOUN |  noun |
|   NUM |  numeral |
|   PART |  particle |
|   PRON |  pronoun |
|   PUNCT |  punctuation |
|   SCONJ |  subordinating conjunction |
|   VERB |  verb |
|   X |  other |

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("hamedkhaledi/persain-flair-upos")

# make example sentence
sentence = Sentence("مقامات مصری به خاطر حفظ ثبات کشور در منطقهای پرآشوب بر خود میبالند .")

tagger.predict(sentence)
#print result
print(sentence.to_tagged_string())
```

This yields the following output:
```
مقامات <NOUN> مصری <ADJ> به <ADP> خاطر <NOUN> حفظ <NOUN> ثبات <NOUN> کشور <NOUN> در <ADP> منطقهای <NOUN> پرآشوب <ADJ> بر <ADP> خود <PRON> میبالند <VERB> . <PUNCT>
```

---

### Results
- F-score (micro) 0.9773
- F-score (macro) 0.9461
- Accuracy 0.9773

```
By class:
              precision    recall  f1-score   support

        NOUN     0.9770    0.9849    0.9809      6420
         ADP     0.9947    0.9916    0.9932      1909
         ADJ     0.9342    0.9128    0.9234      1525
       PUNCT     1.0000    1.0000    1.0000      1365
        VERB     0.9840    0.9711    0.9775      1141
       CCONJ     0.9912    0.9937    0.9925       794
         AUX     0.9622    0.9799    0.9710       546
        PRON     0.9751    0.9865    0.9808       517
       SCONJ     0.9797    0.9757    0.9777       494
         NUM     0.9948    1.0000    0.9974       385
         ADV     0.9343    0.9033    0.9185       362
         DET     0.9773    0.9711    0.9742       311
        PART     0.9916    1.0000    0.9958       237
        INTJ     0.8889    0.8000    0.8421        10
           X     0.7143    0.6250    0.6667         8

   micro avg     0.9773    0.9773    0.9773     16024
   macro avg     0.9533    0.9397    0.9461     16024
weighted avg     0.9772    0.9773    0.9772     16024
 samples avg     0.9773    0.9773    0.9773     16024

Loss: 0.12471389770507812

```