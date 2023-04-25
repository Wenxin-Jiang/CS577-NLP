---
tags:
- flair
- hunflair
- token-classification
- sequence-tagger-model
language: en
widget:
- text: "Isolate an enhancer element located between -89 and -50 bp in PAI-1"
---

## HunFlair model for ENHANCER  

[HunFlair](https://github.com/flairNLP/flair/blob/master/resources/docs/HUNFLAIR.md) (biomedical flair) for enhancer entity.


Predicts 1 tag:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| Enhancer         | DNA enhancer region | 

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
tagger = SequenceTagger.load("regel-corpus/hunflair-promoter")

text = "An upstream activator of the mitogen-activated protein (MAP) kinase pathways was used to isolate an enhancer element located between -89 and -50 bp in PAI-1 promoter that was activated by MEKK-1."

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
Span [18,19,20,21,22,23,24,25,26,27,28,29,30]: "enhancer element located between - 89 and - 50 bp in PAI-1 promoter"   [− Labels: Enhancer (0.992)]
```

So, the entity "*enhancer element located between - 89 and - 50 bp in PAI-1*" (labeled as a **enhancer**) is found in the sentence. 

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



