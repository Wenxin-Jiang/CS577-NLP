---
tags:
- flair
- token-classification
- sequence-tagger-model
language: de
datasets:
- conll2003
inference: false
---

## Flair NER model `de-ner-conll03-v0.4.pt`

Imported from https://nlp.informatik.hu-berlin.de/resources/models/de-ner/

### Demo: How to use in Flair

```python
from flair.data import Sentence
from flair.models import SequenceTagger

sentence = Sentence(
	"Mein Name ist Julien, ich lebe zurzeit in Paris, ich arbeite bei Hugging Face, Inc."
)

tagger = SequenceTagger.load("julien-c/flair-de-ner")


# predict NER tags
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence.to_tagged_string())


```

yields the following output:

> `Mein Name ist Julien <S-PER> , ich lebe zurzeit in Paris <S-LOC> , ich arbeite bei Hugging <B-ORG> Face <E-ORG> , Inc <S-ORG> .`

### Thanks [@stefan-it](https://huggingface.co/stefan-it) for the Flair integration ❤️ 🔥

