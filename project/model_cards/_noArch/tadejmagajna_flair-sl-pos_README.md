---
tags:
- flair
- token-classification
- sequence-tagger-model
language: sl
widget:
- text: "Danes je lep dan."
---

## Slovene Part-of-speech (PoS) Tagging for Flair

This is a Slovene part-of-speech (PoS) tagger trained on the [Slovenian UD Treebank](https://github.com/UniversalDependencies/UD_Slovenian-SSJ) using Flair NLP framework.

The tagger is trained using a combination of forward Slovene contextual string embeddings, backward Slovene contextual string embeddings and classic Slovene FastText embeddings.

F-score (micro): **94,96**

The model is trained on a large (500+) number of different tags that described at [https://universaldependencies.org/tagset-conversion/sl-multext-uposf.html](https://universaldependencies.org/tagset-conversion/sl-multext-uposf.html).

Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

---
### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)
```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("tadejmagajna/flair-sl-pos")

# make example sentence
sentence = Sentence("Danes je lep dan.")

# predict PoS tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted PoS spans
print('The following PoS tags are found:')
# iterate over parts of speech and print
for tag in sentence.get_spans('pos'):
    print(tag)
```

This prints out the following output:
```
Sentence: "Danes je lep dan ."   [− Tokens: 5  − Token-Labels: "Danes <Rgp> je <Va-r3s-n> lep <Agpmsnn> dan <Ncmsn> . <Z>"]
The following PoS tags are found:
Span [1]: "Danes"   [− Labels: Rgp (1.0)]
Span [2]: "je"   [− Labels: Va-r3s-n (1.0)]
Span [3]: "lep"   [− Labels: Agpmsnn (0.9999)]
Span [4]: "dan"   [− Labels: Ncmsn (1.0)]
Span [5]: "."   [− Labels: Z (1.0)]
```

---
### Training: Script to train this model
The following standard Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import UD_SLOVENIAN
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. get the corpus
corpus: Corpus = UD_SLOVENIAN()

# 2. what tag do we want to predict?
tag_type = 'pos'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize embeddings
embedding_types = [
    WordEmbeddings('sl'),
    FlairEmbeddings('sl-forward'),
    FlairEmbeddings('sl-backward'),
]
embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type)

# 6. initialize trainer
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 7. start training
trainer.train('resources/taggers/pos-slovene',
              train_with_dev=True,
              max_epochs=150)
```

---
### Cite
Please cite the following paper when using this model.
```
@inproceedings{akbik2018coling,
  title={Contextual String Embeddings for Sequence Labeling},
  author={Akbik, Alan and Blythe, Duncan and Vollgraf, Roland},
  booktitle = {{COLING} 2018, 27th International Conference on Computational Linguistics},
  pages     = {1638--1649},
  year      = {2018}
}
```
---
### Issues?
The Flair issue tracker is available [here](https://github.com/flairNLP/flair/issues/).