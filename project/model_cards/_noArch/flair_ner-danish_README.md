---
tags:
- flair
- token-classification
- sequence-tagger-model
language: da
datasets:
- DaNE
widget:
- text: "Jens Peter Hansen kommer fra Danmark"
---

# Danish NER in Flair (default model)

This is the standard 4-class NER model for Danish that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **81.78** (DaNER)

Predicts 4 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| PER         | person name | 
| LOC         | location name | 
| ORG         | organization name | 
| MISC         | other name | 

Based on Transformer embeddings and LSTM-CRF.

---
# Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-danish")

# make example sentence
sentence = Sentence("Jens Peter Hansen kommer fra Danmark")

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
Span [1,2,3]: "Jens Peter Hansen"   [− Labels: PER (0.9961)]
Span [6]: "Danmark"   [− Labels: LOC (0.9816)]
```

So, the entities "*Jens Peter Hansen*" (labeled as a **person**) and "*Danmark*" (labeled as a **location**) are found in the sentence "*Jens Peter Hansen kommer fra Danmark*". 


---

### Training: Script to train this model

The model was trained by the [DaNLP project](https://github.com/alexandrainst/danlp) using the [DaNE corpus](https://github.com/alexandrainst/danlp/blob/master/docs/docs/datasets.md#danish-dependency-treebank-dane-dane). Check their repo for more information.

The following Flair script may be used to train such a model: 

```python
from flair.data import Corpus
from flair.datasets import DANE
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. get the corpus
corpus: Corpus = DANE()

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

    # GloVe embeddings
    WordEmbeddings('da'),

    # contextual string embeddings, forward
    FlairEmbeddings('da-forward'),

    # contextual string embeddings, backward
    FlairEmbeddings('da-backward'),
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
trainer.train('resources/taggers/ner-danish',
              train_with_dev=True,
              max_epochs=150)
```


---

### Cite

Please cite the following papers when using this model.

```
@inproceedings{akbik-etal-2019-flair,
    title = "{FLAIR}: An Easy-to-Use Framework for State-of-the-Art {NLP}",
    author = "Akbik, Alan  and
      Bergmann, Tanja  and
      Blythe, Duncan  and
      Rasul, Kashif  and
      Schweter, Stefan  and
      Vollgraf, Roland",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics (Demonstrations)",
    year = "2019",
    url = "https://www.aclweb.org/anthology/N19-4010",
    pages = "54--59",
}
```

And check the [DaNLP project](https://github.com/alexandrainst/danlp) for more information.

---

### Issues?

The Flair issue tracker is available [here](https://github.com/flairNLP/flair/issues/).
