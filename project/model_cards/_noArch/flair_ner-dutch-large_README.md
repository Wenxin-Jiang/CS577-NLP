---
tags:
- flair
- token-classification
- sequence-tagger-model
language: nl
datasets:
- conll2003
widget:
- text: "George Washington ging naar Washington"
---

## Dutch NER in Flair (large model)

This is the large 4-class NER model for Dutch that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **95,25** (CoNLL-03 Dutch)

Predicts 4 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| PER         | person name | 
| LOC         | location name | 
| ORG         | organization name | 
| MISC         | other name | 

Based on document-level XLM-R embeddings and [FLERT](https://arxiv.org/pdf/2011.06993v1.pdf/).

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-dutch-large")

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
Span [1,2]: "George Washington"   [− Labels: PER (1.0)]
Span [5]: "Washington"   [− Labels: LOC (1.0)]
```

So, the entities "*George Washington*" (labeled as a **person**) and "*Washington*" (labeled as a **location**) are found in the sentence "*George Washington ging naar Washington*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
import torch

# 1. get the corpus
from flair.datasets import CONLL_03_DUTCH

corpus = CONLL_03_DUTCH()

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

trainer.train('resources/taggers/ner-dutch-large',
              learning_rate=5.0e-6,
              mini_batch_size=4,
              mini_batch_chunk_size=1,
              max_epochs=20,
              scheduler=OneCycleLR,
              embeddings_storage_mode='none',
              weight_decay=0.,
              )

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
