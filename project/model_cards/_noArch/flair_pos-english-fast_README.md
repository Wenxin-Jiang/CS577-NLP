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

## English Part-of-Speech Tagging in Flair (fast model)

This is the fast part-of-speech tagging model for English that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **98,10** (Ontonotes)

Predicts fine-grained POS tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
|ADD        | Email |
|AFX        | Affix |
|CC         | Coordinating conjunction  |
|CD         | Cardinal number |
|DT         | Determiner |
|EX         | Existential there |
|FW         | Foreign word |
|HYPH       | Hyphen |
|IN        | Preposition or subordinating conjunction |
|JJ         | Adjective |
|JJR        |Adjective, comparative |
|JJS        | Adjective, superlative |
|LS         | List item marker  |
|MD         | Modal |
|NFP        | Superfluous punctuation |
|NN        | Noun, singular or mass |
|NNP        |Proper noun, singular |
|NNPS       | Proper noun, plural |
|NNS        |Noun, plural |
|PDT        | Predeterminer |
|POS        | Possessive ending |
|PRP        | Personal pronoun |
|PRP$       | Possessive pronoun |
|RB         | Adverb |
|RBR        | Adverb, comparative |
|RBS        | Adverb, superlative |
|RP         | Particle |
|SYM        | Symbol |
|TO         | to |
|UH         | Interjection |
|VB         | Verb, base form |
|VBD       | Verb, past tense |
|VBG        | Verb, gerund or present participle |
|VBN        | Verb, past participle |
|VBP        | Verb, non-3rd person singular present |
|VBZ        | Verb, 3rd person singular present |
|WDT        | Wh-determiner |
|WP        | Wh-pronoun |
|WP$        | Possessive wh-pronoun |
|WRB        | Wh-adverb |
|XX         | Unknown |



Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/pos-english-fast")

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
Span [1]: "I"   [− Labels: PRP (1.0)]
Span [2]: "love"   [− Labels: VBP (0.9998)]
Span [3]: "Berlin"   [− Labels: NNP (0.9999)]
Span [4]: "."   [− Labels: . (0.9998)]

```

So, the word "*I*" is labeled as a **pronoun** (PRP),  "*love*" is labeled as a **verb** (VBP) and "*Berlin*" is labeled as a **proper noun** (NNP) in the sentence "*I love Berlin*". 


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
tag_type = 'pos'

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
trainer.train('resources/taggers/pos-english-fast',
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
