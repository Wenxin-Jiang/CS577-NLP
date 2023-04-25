---
tags:
- flair
- token-classification
- sequence-tagger-model
language: fa
datasets:
- UPC-2017
widget:
- text: "تمام ایران یک تابستان تنوری را تجربه میکند ."
---

## Persian Part-of-Speech Tagging in Flair

This is the part-of-speech tagging model for Persian that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **??** (UPC-2017)

 List of Tags in UPC:

| **tag**  |       **meaning**       |
|:--------:|:-----------------------:|
|   ADJ    |        adjective        |
| ADJ_CMPR |  Comparative adjective  |
| ADJ_INO  |  Participle adjective   |
| ADJ_SUP  |  Superlative adjective  |
| ADJ_VOC  |   Vocative adjective    |
|   ADV    |         Adverb          |
| ADV_COMP |  Adverb of comparison   |
|  ADV_I   | Adverb of interrogation |
| ADV_LOC  |   Adverb of location    |
| ADV_NEG  |   Adverb of negation    |
| ADV_TIME |     Adverb of time      |
|  CLITIC  |    Accusative marker    |
|   CON    |       Conjunction       |
|   DELM   |        Delimiter        |
|   DET    |       Determiner        |
|    FW    |      Foreign Word       |
|   INT    |      Interjection       |
|   N_PL   |       Plural noun       |
|  N_SING  |      Singular noun      |
|   NUM    |         Numeral         |
|  N_VOC   |      Vocative noun      |
|    P     |       Preposition       |
|    PREV      |       Preverbal particle       |
|    PRO      |       Pronoun       |
|    SYM     |       Symbol       |
|    V_AUX     |       Auxiliary verb       |
|    V_PA     |       Past tense verb       |
|    V_PP     |       Past participle verb       |
|    V_PRS     |       Present tense verb       |
|    V_SUB     |       Subjunctive verb       |

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("hamedkhaledi/persain-flair-pos")

# make example sentence
sentence = Sentence("تمام ایران یک تابستان تنوری را تجربه میکند .")

tagger.predict(sentence)
# print result
print(sentence.to_tagged_string())
```

This yields the following output:

```
تمام <DET> ایران <N_SING> یک <NUM> تابستان <N_SING> تنوری <ADJ> را <CLITIC> تجربه <N_SING> میکند <V_PRS> . <DELM>
```