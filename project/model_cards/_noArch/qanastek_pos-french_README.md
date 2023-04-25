---
tags:
- flair
- token-classification
- sequence-tagger-model
language: fr
datasets:
- qanastek/ANTILLES
widget:
- text: "George Washington est allé à Washington"
---

# POET: A French Extended Part-of-Speech Tagger

- Corpora: [ANTILLES](https://github.com/qanastek/ANTILLES)
- Embeddings: [FastText](https://fasttext.cc/)
- Sequence Labelling: [Bi-LSTM-CRF](https://arxiv.org/abs/1011.4088)
- Number of Epochs: 115

**People Involved**

* [LABRAK Yanis](https://www.linkedin.com/in/yanis-labrak-8a7412145/) (1)
* [DUFOUR Richard](https://cv.archives-ouvertes.fr/richard-dufour) (2)

**Affiliations**

1. [LIA, NLP team](https://lia.univ-avignon.fr/), Avignon University, Avignon, France.
2. [LS2N, TALN team](https://www.ls2n.fr/equipe/taln/), Nantes University, Nantes, France.

## Demo: How to use in Flair

Requires [Flair](https://pypi.org/project/flair/): ```pip install flair```

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# Load the model
model = SequenceTagger.load("qanastek/pos-french")

sentence = Sentence("George Washington est allé à Washington")

# Predict tags
model.predict(sentence)

# Print predicted pos tags
print(sentence.to_tagged_string())
```

Output:

![Preview Output](preview.PNG)

## Training data

`ANTILLES` is a part-of-speech tagging corpora based on [UD_French-GSD](https://universaldependencies.org/treebanks/fr_gsd/index.html) which was originally created in 2015 and is based on the [universal dependency treebank v2.0](https://github.com/ryanmcd/uni-dep-tb).

Originally, the corpora consists of 400,399 words (16,341 sentences) and had 17 different classes. Now, after applying our tags augmentation we obtain 60 different classes which add linguistic and semantic information such as the gender, number, mood, person, tense or verb form given in the different CoNLL-03 fields from the original corpora.

We based our tags on the level of details given by the [LIA_TAGG](http://pageperso.lif.univ-mrs.fr/frederic.bechet/download.html) statistical POS tagger written by [Frédéric Béchet](http://pageperso.lif.univ-mrs.fr/frederic.bechet/index-english.html) in 2001.

The corpora used for this model is available on [Github](https://github.com/qanastek/ANTILLES) at the [CoNLL-U format](https://universaldependencies.org/format.html).

Training data are fed to the model as free language and doesn't pass a normalization phase. Thus, it's made the model case and punctuation sensitive.

## Original Tags

```plain
PRON VERB SCONJ ADP CCONJ DET NOUN ADJ AUX ADV PUNCT PROPN NUM SYM PART X INTJ
```

## New additional POS tags

| Abbreviation | Description | Examples |
|:--------:|:--------:|:--------:|
| PREP | Preposition | de |
| AUX | Auxiliary Verb | est |
| ADV | Adverb | toujours |
| COSUB | Subordinating conjunction | que |
| COCO | Coordinating Conjunction | et |
| PART | Demonstrative particle | -t |
| PRON | Pronoun | qui ce quoi |
| PDEMMS | Demonstrative Pronoun - Singular Masculine | ce |
| PDEMMP | Demonstrative Pronoun - Plural Masculine | ceux |
| PDEMFS | Demonstrative Pronoun - Singular Feminine | cette |
| PDEMFP | Demonstrative Pronoun - Plural Feminine | celles |
| PINDMS | Indefinite Pronoun - Singular Masculine | tout |
| PINDMP | Indefinite Pronoun - Plural Masculine | autres |
| PINDFS | Indefinite Pronoun - Singular Feminine | chacune |
| PINDFP | Indefinite Pronoun - Plural Feminine | certaines |
| PROPN | Proper noun | Houston |
| XFAMIL | Last name | Levy |
| NUM | Numerical Adjective | trentaine vingtaine |
| DINTMS | Masculine Numerical Adjective | un |
| DINTFS | Feminine Numerical Adjective | une |
| PPOBJMS | Pronoun complements of objects - Singular Masculine | le lui |
| PPOBJMP | Pronoun complements of objects - Plural Masculine | eux y |
| PPOBJFS | Pronoun complements of objects - Singular Feminine | moi la |
| PPOBJFP | Pronoun complements of objects - Plural Feminine | en y |
| PPER1S | Personal Pronoun First-Person - Singular | je |
| PPER2S | Personal Pronoun Second-Person - Singular | tu |
| PPER3MS | Personal Pronoun Third-Person - Singular Masculine | il |
| PPER3MP | Personal Pronoun Third-Person - Plural Masculine | ils |
| PPER3FS | Personal Pronoun Third-Person - Singular Feminine | elle |
| PPER3FP | Personal Pronoun Third-Person - Plural Feminine | elles |
| PREFS | Reflexive Pronoun First-Person - Singular | me m' |
| PREF | Reflexive Pronoun Third-Person - Singular | se s' |
| PREFP | Reflexive Pronoun First / Second-Person - Plural | nous vous |
| VERB | Verb | obtient |
| VPPMS | Past Participle - Singular Masculine | formulé |
| VPPMP | Past Participle - Plural Masculine | classés |
| VPPFS | Past Participle - Singular Feminine | appelée |
| VPPFP | Past Participle - Plural Feminine | sanctionnées |
| DET | Determinant | les l' |
| DETMS | Determinant - Singular Masculine | les |
| DETFS | Determinant - Singular Feminine | la |
| ADJ | Adjective | capable sérieux |
| ADJMS | Adjective - Singular Masculine | grand important |
| ADJMP | Adjective - Plural Masculine | grands petits |
| ADJFS | Adjective - Singular Feminine | française petite |
| ADJFP | Adjective - Plural Feminine | légères petites |
| NOUN | Noun | temps |
| NMS | Noun - Singular Masculine | drapeau |
| NMP | Noun - Plural Masculine | journalistes |
| NFS | Noun - Singular Feminine | tête |
| NFP | Noun - Plural Feminine | ondes |
| PREL | Relative Pronoun | qui dont |
| PRELMS | Relative Pronoun - Singular Masculine | lequel |
| PRELMP | Relative Pronoun - Plural Masculine | lesquels |
| PRELFS | Relative Pronoun - Singular Feminine | laquelle |
| PRELFP | Relative Pronoun - Plural Feminine | lesquelles |
| INTJ | Interjection | merci bref |
| CHIF | Numbers | 1979 10 |
| SYM | Symbol | € % |
| YPFOR | Endpoint | . |
| PUNCT | Ponctuation | : , |
| MOTINC | Unknown words | Technology Lady |
| X | Typos & others | sfeir 3D statu |

## Evaluation results

The test corpora used for this evaluation is available on [Github](https://github.com/qanastek/ANTILLES/blob/main/ANTILLES/test.conllu).

```plain
Results:
- F-score (micro): 0.952
- F-score (macro): 0.8644
- Accuracy (incl. no class): 0.952

By class:
              precision    recall  f1-score   support
      PPER1S     0.9767    1.0000    0.9882        42
        VERB     0.9823    0.9537    0.9678       583
       COSUB     0.9344    0.8906    0.9120       128
       PUNCT     0.9878    0.9688    0.9782       833
        PREP     0.9767    0.9879    0.9822      1483
      PDEMMS     0.9583    0.9200    0.9388        75
        COCO     0.9839    1.0000    0.9919       245
         DET     0.9679    0.9814    0.9746       645
         NMP     0.9521    0.9115    0.9313       305
       ADJMP     0.8352    0.9268    0.8786        82
        PREL     0.9324    0.9857    0.9583        70
       PREFP     0.9767    0.9545    0.9655        44
         AUX     0.9537    0.9859    0.9695       355
         ADV     0.9440    0.9365    0.9402       504
       VPPMP     0.8667    1.0000    0.9286        26
      DINTMS     0.9919    1.0000    0.9959       122
       ADJMS     0.9020    0.9057    0.9039       244
         NMS     0.9226    0.9336    0.9281       753
         NFS     0.9347    0.9714    0.9527       560
       YPFOR     0.9806    1.0000    0.9902       353
      PINDMS     1.0000    0.9091    0.9524        44
        NOUN     0.8400    0.5385    0.6562        39
       PROPN     0.8605    0.8278    0.8439       395
       DETMS     0.9972    0.9972    0.9972       362
     PPER3MS     0.9341    0.9770    0.9551        87
       VPPMS     0.8994    0.9682    0.9325       157
       DETFS     1.0000    1.0000    1.0000       240
       ADJFS     0.9266    0.9011    0.9136       182
       ADJFP     0.9726    0.9342    0.9530        76
         NFP     0.9463    0.9749    0.9604       199
       VPPFS     0.8000    0.9000    0.8471        40
        CHIF     0.9543    0.9414    0.9478       222
      XFAMIL     0.9346    0.8696    0.9009       115
     PPER3MP     0.9474    0.9000    0.9231        20
     PPOBJMS     0.8800    0.9362    0.9072        47
        PREF     0.8889    0.9231    0.9057        52
     PPOBJMP     1.0000    0.6000    0.7500        10
         SYM     0.9706    0.8684    0.9167        38
      DINTFS     0.9683    1.0000    0.9839        61
      PDEMFS     1.0000    0.8966    0.9455        29
     PPER3FS     1.0000    0.9444    0.9714        18
       VPPFP     0.9500    1.0000    0.9744        19
        PRON     0.9200    0.7419    0.8214        31
     PPOBJFS     0.8333    0.8333    0.8333         6
        PART     0.8000    1.0000    0.8889         4
     PPER3FP     1.0000    1.0000    1.0000         2
      MOTINC     0.3571    0.3333    0.3448        15
      PDEMMP     1.0000    0.6667    0.8000         3
        INTJ     0.4000    0.6667    0.5000         6
       PREFS     1.0000    0.5000    0.6667        10
         ADJ     0.7917    0.8636    0.8261        22
      PINDMP     0.0000    0.0000    0.0000         1
      PINDFS     1.0000    1.0000    1.0000         1
         NUM     1.0000    0.3333    0.5000         3
      PPER2S     1.0000    1.0000    1.0000         2
     PPOBJFP     1.0000    0.5000    0.6667         2
      PDEMFP     1.0000    0.6667    0.8000         3
           X     0.0000    0.0000    0.0000         1
      PRELMS     1.0000    1.0000    1.0000         2
      PINDFP     1.0000    1.0000    1.0000         1

    accuracy                         0.9520     10019
   macro avg     0.8956    0.8521    0.8644     10019
weighted avg     0.9524    0.9520    0.9515     10019
```

## BibTeX Citations

Please cite the following paper when using this model.

ANTILLES corpus and POET taggers:

```latex
@inproceedings{labrak:hal-03696042,
  TITLE = {{ANTILLES: An Open French Linguistically Enriched Part-of-Speech Corpus}},
  AUTHOR = {Labrak, Yanis and Dufour, Richard},
  URL = {https://hal.archives-ouvertes.fr/hal-03696042},
  BOOKTITLE = {{25th International Conference on Text, Speech and Dialogue (TSD)}},
  ADDRESS = {Brno, Czech Republic},
  PUBLISHER = {{Springer}},
  YEAR = {2022},
  MONTH = Sep,
  KEYWORDS = {Part-of-speech corpus ; POS tagging ; Open tools ; Word embeddings ; Bi-LSTM ; CRF ; Transformers},
  PDF = {https://hal.archives-ouvertes.fr/hal-03696042/file/ANTILLES_A_freNch_linguisTIcaLLy_Enriched_part_of_Speech_corpus.pdf},
  HAL_ID = {hal-03696042},
  HAL_VERSION = {v1},
}
```

UD_French-GSD corpora:

```latex
@misc{
    universaldependencies,
    title={UniversalDependencies/UD_French-GSD},
    url={https://github.com/UniversalDependencies/UD_French-GSD}, journal={GitHub},
    author={UniversalDependencies}
}
```

LIA TAGG:

```latex
@techreport{LIA_TAGG,
  author = {Frédéric Béchet},
  title = {LIA_TAGG: a statistical POS tagger + syntactic bracketer},
  institution = {Aix-Marseille University & CNRS},
  year = {2001}
}
```

Flair Embeddings:

```latex
@inproceedings{akbik2018coling,
  title={Contextual String Embeddings for Sequence Labeling},
  author={Akbik, Alan and Blythe, Duncan and Vollgraf, Roland},
  booktitle = {{COLING} 2018, 27th International Conference on Computational Linguistics},
  pages     = {1638--1649},
  year      = {2018}
}
```

## Acknowledgment

This work was financially supported by [Zenidoc](https://zenidoc.fr/)
