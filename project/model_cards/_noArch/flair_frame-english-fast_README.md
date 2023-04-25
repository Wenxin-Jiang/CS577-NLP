---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
datasets:
- ontonotes
widget:
- text: "George returned to Berlin to return his hat."
---

## English Verb Disambiguation in Flair (fast model)

This is the fast verb disambiguation model for English that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **88,27** (Ontonotes) - predicts [Proposition Bank verb frames](http://verbs.colorado.edu/propbank/framesets-english-aliases/).

Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/frame-english-fast")

# make example sentence
sentence = Sentence("George returned to Berlin to return his hat.")

# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following frame tags are found:')
# iterate over entities and print
for entity in sentence.get_spans('frame'):
    print(entity)

```

This yields the following output:
```
Span [2]: "returned"   [− Labels: return.01 (0.9867)]
Span [6]: "return"   [− Labels: return.02 (0.4741)]
```

So, the word "*returned*" is labeled as **return.01** (as in *go back somewhere*) while "*return*" is labeled as **return.02** (as in *give back something*) in the sentence "*George returned to Berlin to return his hat*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. load the corpus (Ontonotes does not ship with Flair, you need to download and reformat into a column format yourself)
corpus = ColumnCorpus(
    "resources/tasks/srl", column_format={1: "text", 11: "frame"}
)

# 2. what tag do we want to predict?
tag_type = 'frame'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

    BytePairEmbeddings("en"),

    FlairEmbeddings("news-forward-fast"),

    FlairEmbeddings("news-backward-fast"),
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
trainer.train('resources/taggers/frame-english-fast',
              train_with_dev=True,
              max_epochs=150)
```



---

### Cite

Please cite the following paper when using this model.

```
@inproceedings{akbik2019flair,
  title={FLAIR: An easy-to-use framework for state-of-the-art NLP},
  author={Akbik, Alan and Bergmann, Tanja and Blythe, Duncan and Rasul, Kashif and Schweter, Stefan and Vollgraf, Roland},
  booktitle={{NAACL} 2019, 2019 Conference of the North American Chapter of the Association for Computational Linguistics (Demonstrations)},
  pages={54--59},
  year={2019}
}

```

---

### Issues?

The Flair issue tracker is available [here](https://github.com/flairNLP/flair/issues/).
