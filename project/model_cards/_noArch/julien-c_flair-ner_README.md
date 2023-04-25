---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
datasets:
- conll2003
inference: false
---

## Flair NER model `en-ner-conll03-v0.4.pt`

Imported from https://nlp.informatik.hu-berlin.de/resources/models/ner/

### Demo: How to use in Flair

```python
from flair.data import Sentence
from flair.models import SequenceTagger

sentence = Sentence(
	"My name is Julien, I currently live in Paris, I work at Hugging Face, Inc."
)

tagger = SequenceTagger.load("julien-c/flair-ner")


# predict NER tags
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence.to_tagged_string())


```

yields the following output:

> `My name is Julien <S-PER> , I currently live in Paris <S-LOC> , I work at Hugging <B-LOC> Face <E-LOC> .`


### Thanks [@stefan-it](https://huggingface.co/stefan-it) for the Flair integration ❤️ 🔥

