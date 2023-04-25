---
tags:
- flair
- token-classification
- sequence-tagger-model
language: sv
datasets:
- SUC 3.0
widget:
- text: "Hampus bor i Skåne och har levererat denna model idag."
---

Published with ❤️ from [londogard](https://londogard.com).

## Swedish NER in Flair (SUC 3.0)
F1-Score: **85.6** (SUC 3.0)

Predicts 8 tags:

|**Tag**|**Meaning**|
|---|---|
| PRS| person name | 
| ORG        | organisation name| 
| TME        | time unit | 
| WRK         | building name | 
| LOC         | location name | 
| EVN         | event name | 
| MSR         | measurement unit | 
| OBJ         | object (like "Rolls-Royce" is a object in the form of a special car) | 

Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger
# load tagger
tagger = SequenceTagger.load("londogard/flair-swe-ner")
# make example sentence
sentence = Sentence("Hampus bor i Skåne och har levererat denna model idag.")
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
Span [0]: "Hampus"   [− Labels: PRS (1.0)]
Span [3]: "Skåne"   [− Labels: LOC (1.0)]
Span [9]: "idag"   [− Labels: TME(1.0)]
```

So, the entities "_Hampus_" (labeled as a **PRS**), "_Skåne_" (labeled as a **LOC**), "_idag_" (labeled as a **TME**) are found in the sentence "_Hampus bor i Skåne och har levererat denna model idag._". 

---

**Please mention londogard if using this models.**