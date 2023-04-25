---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
datasets:
- conll2000
widget:
- text: "The happy man has been eating at the diner"
---

## English Chunking in Flair (fast model)

This is the fast phrase chunking model for English that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **96,22** (CoNLL-2000)

Predicts 4 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| ADJP     | adjectival |
| ADVP     | adverbial |
| CONJP     | conjunction |
| INTJ     | interjection |
| LST     | list marker |
| NP     | noun phrase |
| PP     | prepositional |
| PRT     | particle |
| SBAR      | subordinate clause |
| VP      | verb phrase |

Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/chunk-english-fast")

# make example sentence
sentence = Sentence("The happy man has been eating at the diner")

# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following NER tags are found:')
# iterate over entities and print
for entity in sentence.get_spans('np'):
    print(entity)

```

This yields the following output:
```
Span [1,2,3]: "The happy man"   [− Labels: NP (0.9958)]
Span [4,5,6]: "has been eating"   [− Labels: VP (0.8759)]
Span [7]: "at"   [− Labels: PP (1.0)]
Span [8,9]: "the diner"   [− Labels: NP (0.9991)]

```

So, the spans "*The happy man*" and "*the diner*" are labeled as **noun phrases** (NP) and "*has been eating*" is labeled as a **verb phrase** (VP) in the sentence "*The happy man has been eating at the diner*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import CONLL_2000
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. get the corpus
corpus: Corpus = CONLL_2000()

# 2. what tag do we want to predict?
tag_type = 'np'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

    # contextual string embeddings, forward
    FlairEmbeddings('news-forward-fast'),

    # contextual string embeddings, backward
    FlairEmbeddings('news-backward-fast'),
]

# embedding stack consists of Flair and GloVe embeddings
embeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
from flair.models import SequenceTagger

tagger = SequenceTagger(hidden_size=256,
                        embeddings=embeddings,
                        tag_dictionary=tag_dictionary,
                        tag_type=tag_type)

# 6. initialize trainer
from flair.trainers import ModelTrainer

trainer = ModelTrainer(tagger, corpus)

# 7. run training
trainer.train('resources/taggers/chunk-english-fast',
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
