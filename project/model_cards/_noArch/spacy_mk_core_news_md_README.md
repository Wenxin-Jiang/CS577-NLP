---
tags:
- spacy
- token-classification
language:
- mk
license: cc-by-sa-4.0
model-index:
- name: mk_core_news_md
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.7472245944
    - name: NER Recall
      type: recall
      value: 0.7446808511
    - name: NER F Score
      type: f_score
      value: 0.7459505541
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9260857837
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.6771344455
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.5201177625
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.7323943662
---
### Details: https://spacy.io/models/mk#mk_core_news_md

Macedonian pipeline optimized for CPU. Components: tok2vec, morphologizer, parser, senter, ner, attribute_ruler, lemmatizer.

| Feature | Description |
| --- | --- |
| **Name** | `mk_core_news_md` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `morphologizer`, `parser`, `attribute_ruler`, `lemmatizer`, `ner` |
| **Components** | `morphologizer`, `parser`, `senter`, `attribute_ruler`, `lemmatizer`, `ner` |
| **Vectors** | 274587 keys, 20000 unique vectors (300 dimensions) |
| **Sources** | [Macedonian Corpus](https://blog.netcetera.com/macedonian-spacy-f3c85484777f) (Damjan Zlatinov, Melanija Gerasimovska, Borijan Georgievski, Marija Todosovska)<br />[spaCy lookups data](https://github.com/explosion/spacy-lookups-data) (Explosion)<br />[Explosion fastText Vectors (cbow, OSCAR Common Crawl + Wikipedia)](https://spacy.io) (Explosion) |
| **License** | `CC BY-SA 4.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (54 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `POS=PROPN`, `POS=AUX`, `POS=ADJ`, `POS=NOUN`, `POS=ADP`, `POS=PUNCT`, `POS=CONJ`, `POS=NUM`, `POS=VERB`, `POS=PRON`, `POS=ADV`, `POS=SCONJ`, `POS=PART`, `POS=SYM`, `_`, `POS=SPACE`, `POS=X`, `POS=INTJ` |
| **`parser`** | `ROOT`, `advmod`, `att`, `aux`, `cc`, `dep`, `det`, `dobj`, `iobj`, `neg`, `nsubj`, `pobj`, `poss`, `pozm`, `pozv`, `prep`, `punct`, `relcl` |
| **`ner`** | `CARDINAL`, `DATE`, `EVENT`, `FAC`, `GPE`, `LANGUAGE`, `LAW`, `LOC`, `MONEY`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PRODUCT`, `QUANTITY`, `TIME`, `WORK_OF_ART` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_ACC` | 100.00 |
| `TOKEN_P` | 100.00 |
| `TOKEN_R` | 100.00 |
| `TOKEN_F` | 100.00 |
| `SENTS_P` | 80.00 |
| `SENTS_R` | 67.53 |
| `SENTS_F` | 73.24 |
| `DEP_UAS` | 67.71 |
| `DEP_LAS` | 52.01 |
| `ENTS_P` | 74.72 |
| `ENTS_R` | 74.47 |
| `ENTS_F` | 74.60 |
| `POS_ACC` | 92.61 |