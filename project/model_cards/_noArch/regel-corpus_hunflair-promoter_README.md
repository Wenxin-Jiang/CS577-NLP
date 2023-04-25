---
tags:
- flair
- hunflair
- token-classification
- sequence-tagger-model
language: en
widget:
- text: "Two putative extended promoters consensus sequences (p1 and p2)."
---

## HunFlair model for PROMOTER  

[HunFlair](https://github.com/flairNLP/flair/blob/master/resources/docs/HUNFLAIR.md) (biomedical flair) for promoter entity.


Predicts 1 tag:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| Promoter         | DNA promoter region | 

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

text = "The upstream region of the glnA gene contained two putative extended promoter consensus sequences (p1 and p2)."

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
Span [16]: "p1"   [− Labels: Promoter (0.9878)]
Span [18]: "p2"   [− Labels: Promoter (0.9216)]
```

So, the entities "*p1*" and "*p2*" (labeled as a **promoter**)  are found in the sentence.

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




