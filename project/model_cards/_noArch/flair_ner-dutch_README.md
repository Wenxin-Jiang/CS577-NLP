---
tags:
- flair
- token-classification
- sequence-tagger-model
language: nl
datasets:
- conll2003
widget:
- text: "George Washington ging naar Washington."
---

# Dutch NER in Flair (default model)

This is the standard 4-class NER model for Dutch that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **92,58** (CoNLL-03)

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
tagger = SequenceTagger.load("flair/ner-dutch")

# make example sentence
sentence = Sentence("George Washington ging naar Washington")

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
Span [1,2]: "George Washington"   [− Labels: PER (0.997)]
Span [5]: "Washington"   [− Labels: LOC (0.9996)]
```

So, the entities "*George Washington*" (labeled as a **person**) and "*Washington*" (labeled as a **location**) are found in the sentence "*George Washington ging naar Washington*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import CONLL_03_DUTCH
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings


# 1. get the corpus
corpus: Corpus = CONLL_03_DUTCH()

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize embeddings
embeddings = TransformerWordEmbeddings('wietsedv/bert-base-dutch-cased')

# 5. initialize sequence tagger
tagger: SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type)

# 6. initialize trainer
trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 7. run training
trainer.train('resources/taggers/ner-dutch',
              train_with_dev=True,
              max_epochs=150)
```


---

### Cite

Please cite the following paper when using this model.

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

---

### Issues?

The Flair issue tracker is available [here](https://github.com/flairNLP/flair/issues/).
