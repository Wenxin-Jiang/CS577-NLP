---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
datasets:
- ontonotes
widget:
- text: "On September 1st George won 1 dollar while watching Game of Thrones."
---

## English NER in Flair (Ontonotes large model)

This is the large 18-class NER model for English that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **90.93** (Ontonotes)

Predicts 18 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| CARDINAL    | cardinal value | 
| DATE         | date value | 
| EVENT         | event name | 
| FAC         | building name | 
| GPE         | geo-political entity | 
| LANGUAGE         | language name | 
| LAW         | law name | 
| LOC         | location name | 
| MONEY         | money name | 
| NORP         | affiliation | 
| ORDINAL         | ordinal value | 
| ORG         | organization name | 
| PERCENT         | percent value | 
| PERSON         | person name | 
| PRODUCT         | product name | 
| QUANTITY         | quantity value | 
| TIME         | time value | 
| WORK_OF_ART         | name of work of art | 

Based on document-level XLM-R embeddings and [FLERT](https://arxiv.org/pdf/2011.06993v1.pdf/).

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-english-ontonotes-large")

# make example sentence
sentence = Sentence("On September 1st George won 1 dollar while watching Game of Thrones.")

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
Span [2,3]: "September 1st"   [− Labels: DATE (1.0)]
Span [4]: "George"   [− Labels: PERSON (1.0)]
Span [6,7]: "1 dollar"   [− Labels: MONEY (1.0)]
Span [10,11,12]: "Game of Thrones"   [− Labels: WORK_OF_ART (1.0)]
```

So, the entities "*September 1st*" (labeled as a **date**), "*George*" (labeled as a **person**), "*1 dollar*" (labeled as a **money**) and "Game of Thrones" (labeled as a **work of art**) are found in the sentence "*On September 1st George Washington won 1 dollar while watching Game of Thrones*". 


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
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize fine-tuneable transformer embeddings WITH document context
from flair.embeddings import TransformerWordEmbeddings

embeddings = TransformerWordEmbeddings(
    model='xlm-roberta-large',
    layers="-1",
    subtoken_pooling="first",
    fine_tune=True,
    use_context=True,
)

# 5. initialize bare-bones sequence tagger (no CRF, no RNN, no reprojection)
from flair.models import SequenceTagger

tagger = SequenceTagger(
    hidden_size=256,
    embeddings=embeddings,
    tag_dictionary=tag_dictionary,
    tag_type='ner',
    use_crf=False,
    use_rnn=False,
    reproject_embeddings=False,
)

# 6. initialize trainer with AdamW optimizer
from flair.trainers import ModelTrainer

trainer = ModelTrainer(tagger, corpus, optimizer=torch.optim.AdamW)

# 7. run training with XLM parameters (20 epochs, small LR)
from torch.optim.lr_scheduler import OneCycleLR

trainer.train('resources/taggers/ner-english-ontonotes-large',
              learning_rate=5.0e-6,
              mini_batch_size=4,
              mini_batch_chunk_size=1,
              max_epochs=20,
              scheduler=OneCycleLR,
              embeddings_storage_mode='none',
              weight_decay=0.,
              )
```



---

### Cite

Please cite the following paper when using this model.

```
@misc{schweter2020flert,
    title={FLERT: Document-Level Features for Named Entity Recognition},
    author={Stefan Schweter and Alan Akbik},
    year={2020},
    eprint={2011.06993},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

---

### Issues?

The Flair issue tracker is available [here](https://github.com/flairNLP/flair/issues/).
