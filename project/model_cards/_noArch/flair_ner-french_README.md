---
tags:
- flair
- token-classification
- sequence-tagger-model
language: fr
datasets:
- conll2003
widget:
- text: "George Washington est allé à Washington"
---

## French NER in Flair (default model)

This is the standard 4-class NER model for French that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **90,61** (WikiNER)

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
tagger = SequenceTagger.load("flair/ner-french")

# make example sentence
sentence = Sentence("George Washington est allé à Washington")

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
Span [1,2]: "George Washington"   [− Labels: PER (0.7394)]
Span [6]: "Washington"   [− Labels: LOC (0.9161)]
```

So, the entities "*George Washington*" (labeled as a **person**) and "*Washington*" (labeled as a **location**) are found in the sentence "*George Washington est allé à Washington*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import WIKINER_FRENCH
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. get the corpus
corpus: Corpus = WIKINER_FRENCH()

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

    # GloVe embeddings
    WordEmbeddings('fr'),

    # contextual string embeddings, forward
    FlairEmbeddings('fr-forward'),

    # contextual string embeddings, backward
    FlairEmbeddings('fr-backward'),
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
trainer.train('resources/taggers/ner-french',
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
