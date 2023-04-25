---
tags:
- flair
- token-classification
- sequence-tagger-model
language: 
- en 
- de 
- nl 
- es
datasets:
- conll2003
widget:
- text: "George Washington ging nach Washington"
---

## 4-Language NER in Flair (English, German, Dutch and Spanish)

This is the fast 4-class NER model for 4 CoNLL-03 languages that ships with [Flair](https://github.com/flairNLP/flair/). Also kind of works for related languages like French.

F1-Score: **91,51** (CoNLL-03 English), **85,72** (CoNLL-03 German revised), **86,22** (CoNLL-03 Dutch), **85,78** (CoNLL-03 Spanish)


Predicts 4 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| PER         | person name | 
| LOC         | location name | 
| ORG         | organization name | 
| MISC         | other name | 

Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-multi-fast")

# make example sentence in any of the four languages
sentence = Sentence("George Washington ging nach Washington")

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
Span [1,2]: "George Washington"   [− Labels: PER (0.9977)]
Span [5]: "Washington"   [− Labels: LOC (0.9895)]
```

So, the entities "*George Washington*" (labeled as a **person**) and "*Washington*" (labeled as a **location**) are found in the sentence "*George Washington ging nach Washington*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import CONLL_03, CONLL_03_GERMAN, CONLL_03_DUTCH, CONLL_03_SPANISH
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. get the multi-language corpus
corpus: Corpus = MultiCorpus([
    CONLL_03(),         # English corpus
    CONLL_03_GERMAN(),  # German corpus
    CONLL_03_DUTCH(),   # Dutch corpus
    CONLL_03_SPANISH(), # Spanish corpus
    ])

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

    # GloVe embeddings
    WordEmbeddings('glove'),

    # FastText embeddings
    WordEmbeddings('de'),

    # contextual string embeddings, forward
    FlairEmbeddings('multi-forward-fast'),

    # contextual string embeddings, backward
    FlairEmbeddings('multi-backward-fast'),
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
trainer.train('resources/taggers/ner-multi-fast',
              train_with_dev=True,
              max_epochs=150)
```



---

### Cite

Please cite the following papers when using this model.


```
@misc{akbik2019multilingual,
  title={Multilingual sequence labeling with one model},
  author={Akbik, Alan and Bergmann, Tanja and Vollgraf, Roland}
  booktitle = {{NLDL} 2019, Northern Lights Deep Learning Workshop},
  year      = {2019}
}
```


```
@inproceedings{akbik2018coling,
  title={Contextual String Embeddings for Sequence Labeling},
  author={Akbik, Alan and Blythe, Duncan and Vollgraf, Roland},
  booktitle = {{COLING} 2018, 27th International Conference on Computational Linguistics},
  pages     = {1638--1649},
  year      = {2018}
}
```
