---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
datasets:
- ontonotes
widget:
- text: "I love Berlin."
---

## English Universal Part-of-Speech Tagging in Flair (default model)

This is the standard universal part-of-speech tagging model for English that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **98,6** (Ontonotes)

Predicts universal POS tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
|ADJ |  adjective |
 |   ADP |  adposition |
 |   ADV |  adverb |
 |   AUX |  auxiliary |
 |   CCONJ |  coordinating conjunction |
 |   DET |  determiner |
 |   INTJ |  interjection |
 |   NOUN |  noun |
 |   NUM |  numeral |
 |   PART |  particle |
 |   PRON |  pronoun |
 |   PROPN |  proper noun |
 |   PUNCT |  punctuation |
 |   SCONJ |  subordinating conjunction |
 |   SYM |  symbol |
 |   VERB |  verb |
 |   X |  other |



Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/upos-english")

# make example sentence
sentence = Sentence("I love Berlin.")

# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following NER tags are found:')
# iterate over entities and print
for entity in sentence.get_spans('pos'):
    print(entity)

```

This yields the following output:
```
Span [1]: "I"   [− Labels: PRON (0.9996)]
Span [2]: "love"   [− Labels: VERB (1.0)]
Span [3]: "Berlin"   [− Labels: PROPN (0.9986)]
Span [4]: "."   [− Labels: PUNCT (1.0)]
```

So, the word "*I*" is labeled as a **pronoun** (PRON),  "*love*" is labeled as a **verb** (VERB) and "*Berlin*" is labeled as a **proper noun** (PROPN) in the sentence "*I love Berlin*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. load the corpus (Ontonotes does not ship with Flair, you need to download and reformat into a column format yourself)
corpus: Corpus = ColumnCorpus(
                "resources/tasks/onto-ner",
                column_format={0: "text", 1: "pos", 2: "upos", 3: "ner"},
                tag_to_bioes="ner",
            )

# 2. what tag do we want to predict?
tag_type = 'upos'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

    # contextual string embeddings, forward
    FlairEmbeddings('news-forward'),

    # contextual string embeddings, backward
    FlairEmbeddings('news-backward'),
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
trainer.train('resources/taggers/upos-english',
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
