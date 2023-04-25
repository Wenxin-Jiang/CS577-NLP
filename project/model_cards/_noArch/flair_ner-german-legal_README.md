---
tags:
- flair
- token-classification
- sequence-tagger-model
language: de
datasets:
- legal
widget:
- text: "Herr W. verstieß gegen § 36 Abs. 7 IfSG."
---

## NER for German Legal Text in Flair (default model)

This is the legal NER model for German that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **96,35** (LER German dataset)

Predicts 19 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| AN   |  Anwalt   |
| EUN   |  Europäische Norm   |
| GS   |  Gesetz   |
| GRT   | Gericht    |
| INN   |  Institution   |
| LD   |  Land   |
| LDS   | Landschaft    |
| LIT   | Literatur    |
| MRK   |  Marke   |
| ORG   |  Organisation   |
| PER   |  Person   |
| RR   |  Richter   |
| RS   |  Rechtssprechung   |
| ST   |  Stadt   |
| STR   |  Straße   |
| UN   |  Unternehmen   |
| VO   |  Verordnung   |
| VS   |  Vorschrift   |
| VT   | Vertrag    |

Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

More details on the Legal NER dataset [here](https://github.com/elenanereiss/Legal-Entity-Recognition)

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-german-legal")

# make example sentence (don't use tokenizer since Rechtstexte are badly handled)
sentence = Sentence("Herr W. verstieß gegen § 36 Abs. 7 IfSG.", use_tokenizer=False)


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
Span [2]: "W."   [− Labels: PER (0.9911)]
Span [5,6,7,8,9]: "§ 36 Abs. 7 IfSG."   [− Labels: GS (0.5353)]

```

So, the entities "*W.*" (labeled as a **person**) and "*§ 36 Abs. 7 IfSG*" (labeled as a **Gesetz**) are found in the sentence "*Herr W. verstieß gegen § 36 Abs. 7 IfSG.*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import LER_GERMAN
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. get the corpus
corpus: Corpus = LER_GERMAN()

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

    # GloVe embeddings
    WordEmbeddings('de'),

    # contextual string embeddings, forward
    FlairEmbeddings('de-forward'),

    # contextual string embeddings, backward
    FlairEmbeddings('de-backward'),
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
trainer.train('resources/taggers/ner-german-legal',
              train_with_dev=True,
              max_epochs=150)
```



---

### Cite

Please cite the following papers when using this model.

```
@inproceedings{leitner2019fine,
  author = {Elena Leitner and Georg Rehm and Julian Moreno-Schneider},
  title = {{Fine-grained Named Entity Recognition in Legal Documents}},
  booktitle = {Semantic Systems. The Power of AI and Knowledge
                  Graphs. Proceedings of the 15th International Conference
                  (SEMANTiCS 2019)},
  year = 2019,
  pages = {272--287},
  pdf = {https://link.springer.com/content/pdf/10.1007%2F978-3-030-33220-4_20.pdf}}
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

---

### Issues?

The Flair issue tracker is available [here](https://github.com/flairNLP/flair/issues/).
