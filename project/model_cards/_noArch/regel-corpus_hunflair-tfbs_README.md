---
tags:
- flair
- hunflair
- token-classification
- sequence-tagger-model
language: en
widget:
- text: "It contains a functional GCGGCGGCG Egr-1-binding site"
---

## HunFlair model for Transcription Factor Binding Site (TFBS)

[HunFlair](https://github.com/flairNLP/flair/blob/master/resources/docs/HUNFLAIR.md) (biomedical flair) for TFBS entity.


Predicts 1 tag:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| Tfbs         | DNA region bound by transcription factor | 

---


### Cite

Please cite the following paper when using this model.

```
@article{garda2022regel,
  title={RegEl corpus: identifying DNA regulatory elements in the scientific literature},
  author={Garda, Samuele and Lenihan-Geels, Freyda and Proft, Sebastian and Hochmuth, Stefanie and Sch{\"u}lke, Markus and Seelow, Dominik and Leser, Ulf},
  journal={Database},
  volume={2022},
  year={2022},
  publisher={Oxford Academic}
}
```


---

### Demo: How to use in Flair

Requires: 
- **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger
# for biomedical-specific tokenization:
# from flair.tokenization import SciSpacyTokenizer

# load tagger
tagger = SequenceTagger.load("regel-corpus/hunflair-tfbs")

text = "We found that Egr-1 specifically binds to the PTEN 5' untranslated region, which contains a functional GCGGCGGCG Egr-1-binding site."

# make example sentence
sentence = Sentence(text)

# for biomedical-specific tokenization:
# sentence = Sentence(text, use_tokenizer=SciSpacyTokenizer())

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
Span [19,20,21]: "GCGGCGGCG Egr-1-binding site"   [− Labels: Tfbs (0.9631)]
```

So, the entity "*GCGGCGGCG Egr-1-binding site*" is found in the sentence. 

Alternatively download all models locally and use the `MultiTagger` class.

```python
from flair.models import MultiTagger

tagger = [
'./models/hunflair-promoter/pytorch_model.bin',
'./models/hunflair-enhancer/pytorch_model.bin',
'./models/hunflair-tfbs/pytorch_model.bin',
]

tagger = MultiTagger.load(['./models/hunflair-'])

tagger.predict(sentence)
```

---



