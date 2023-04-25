---
tags:
- flair
- token-classification
- sequence-tagger-model
language: 
- en 
- de 
- fr 
- it
- nl
- pl
- es
- sv
- da
- no
- fi
- cs
datasets:
- ontonotes
widget:
- text: "Ich liebe Berlin, as they say."
---

## Multilingual Universal Part-of-Speech Tagging in Flair (fast model)

This is the fast multilingual universal part-of-speech tagging model that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **92,88** (12 UD Treebanks covering English, German, French, Italian, Dutch, Polish, Spanish, Swedish, Danish, Norwegian, Finnish and Czech)

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
tagger = SequenceTagger.load("flair/upos-multi-fast")

# make example sentence
sentence = Sentence("Ich liebe Berlin, as they say. ")

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
Span [1]: "Ich"   [− Labels: PRON (0.9999)]
Span [2]: "liebe"   [− Labels: VERB (0.9999)]
Span [3]: "Berlin"   [− Labels: PROPN (0.9997)]
Span [4]: ","   [− Labels: PUNCT (1.0)]
Span [5]: "as"   [− Labels: SCONJ (0.9991)]
Span [6]: "they"   [− Labels: PRON (0.9998)]
Span [7]: "say"   [− Labels: VERB (0.9998)]
Span [8]: "."   [− Labels: PUNCT (1.0)]
```

So, the words "*Ich*" and "*they*" are labeled as **pronouns** (PRON), while "*liebe*" and "*say*" are labeled as **verbs** (VERB) in the multilingual sentence "*Ich liebe Berlin, as they say*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import MultiCorpus
from flair.datasets import UD_ENGLISH, UD_GERMAN, UD_FRENCH, UD_ITALIAN, UD_POLISH, UD_DUTCH, UD_CZECH, \
    UD_DANISH, UD_SPANISH, UD_SWEDISH, UD_NORWEGIAN, UD_FINNISH
from flair.embeddings import StackedEmbeddings, FlairEmbeddings

# 1. make a multi corpus consisting of 12 UD treebanks (in_memory=False here because this corpus becomes large)
corpus = MultiCorpus([
    UD_ENGLISH(in_memory=False),
    UD_GERMAN(in_memory=False),
    UD_DUTCH(in_memory=False),
    UD_FRENCH(in_memory=False),
    UD_ITALIAN(in_memory=False),
    UD_SPANISH(in_memory=False),
    UD_POLISH(in_memory=False),
    UD_CZECH(in_memory=False),
    UD_DANISH(in_memory=False),
    UD_SWEDISH(in_memory=False),
    UD_NORWEGIAN(in_memory=False),
    UD_FINNISH(in_memory=False),
])

# 2. what tag do we want to predict?
tag_type = 'upos'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

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
                        tag_type=tag_type,
                        use_crf=False)

# 6. initialize trainer
from flair.trainers import ModelTrainer

trainer = ModelTrainer(tagger, corpus)

# 7. run training
trainer.train('resources/taggers/upos-multi-fast',
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
