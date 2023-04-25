---
tags:
- flair
- token-classification
- sequence-tagger-model
---
### Demo: How to use in Flair
Requires:
- **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)
```python
from flair.data import Sentence
from flair.models import SequenceTagger
# load tagger
tagger = SequenceTagger.load("GuiGel/meddocan-flair-we-lstm-crf")
# make example sentence
sentence = Sentence("On September 1st George won 1 dollar while watching Game of Thrones.")
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