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
- Embeddings: [Flair](https://aclanthology.org/C18-1139.pdf) & [CamemBERT](https://arxiv.org/abs/1911.03894)
- Sequence Labelling: [Bi-LSTM-CRF](https://arxiv.org/abs/1011.4088)
- Number of Epochs: 50

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

# predict tags
model.predict(sentence)

# print predicted pos tags
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
- F-score (micro) 0.9797
- F-score (macro) 0.9178
- Accuracy 0.9797

By class:
              precision    recall  f1-score   support

        PREP     0.9966    0.9987    0.9976      1483
       PUNCT     1.0000    1.0000    1.0000       833
         NMS     0.9634    0.9801    0.9717       753
         DET     0.9923    0.9984    0.9954       645
        VERB     0.9913    0.9811    0.9862       583
         NFS     0.9667    0.9839    0.9752       560
         ADV     0.9940    0.9821    0.9880       504
       PROPN     0.9541    0.8937    0.9229       395
       DETMS     1.0000    1.0000    1.0000       362
         AUX     0.9860    0.9915    0.9888       355
       YPFOR     1.0000    1.0000    1.0000       353
         NMP     0.9666    0.9475    0.9570       305
        COCO     0.9959    1.0000    0.9980       245
       ADJMS     0.9463    0.9385    0.9424       244
       DETFS     1.0000    1.0000    1.0000       240
        CHIF     0.9648    0.9865    0.9755       222
         NFP     0.9515    0.9849    0.9679       199
       ADJFS     0.9657    0.9286    0.9468       182
       VPPMS     0.9387    0.9745    0.9563       157
       COSUB     1.0000    0.9844    0.9921       128
      DINTMS     0.9918    0.9918    0.9918       122
      XFAMIL     0.9298    0.9217    0.9258       115
     PPER3MS     1.0000    1.0000    1.0000        87
       ADJMP     0.9294    0.9634    0.9461        82
      PDEMMS     1.0000    1.0000    1.0000        75
       ADJFP     0.9861    0.9342    0.9595        76
        PREL     0.9859    1.0000    0.9929        70
      DINTFS     0.9839    1.0000    0.9919        61
        PREF     1.0000    1.0000    1.0000        52
     PPOBJMS     0.9565    0.9362    0.9462        47
       PREFP     0.9778    1.0000    0.9888        44
      PINDMS     1.0000    0.9773    0.9885        44
       VPPFS     0.8298    0.9750    0.8966        40
      PPER1S     1.0000    1.0000    1.0000        42
         SYM     1.0000    0.9474    0.9730        38
        NOUN     0.8824    0.7692    0.8219        39
        PRON     1.0000    0.9677    0.9836        31
      PDEMFS     1.0000    1.0000    1.0000        29
       VPPMP     0.9286    1.0000    0.9630        26
         ADJ     0.9524    0.9091    0.9302        22
     PPER3MP     1.0000    1.0000    1.0000        20
       VPPFP     1.0000    1.0000    1.0000        19
     PPER3FS     1.0000    1.0000    1.0000        18
      MOTINC     0.3333    0.4000    0.3636        15
       PREFS     1.0000    1.0000    1.0000        10
     PPOBJMP     1.0000    0.8000    0.8889        10
     PPOBJFS     0.6250    0.8333    0.7143         6
        INTJ     0.5000    0.6667    0.5714         6
        PART     1.0000    1.0000    1.0000         4
      PDEMMP     1.0000    1.0000    1.0000         3
      PDEMFP     1.0000    1.0000    1.0000         3
     PPER3FP     1.0000    1.0000    1.0000         2
         NUM     1.0000    0.3333    0.5000         3
      PPER2S     1.0000    1.0000    1.0000         2
     PPOBJFP     0.5000    0.5000    0.5000         2
      PRELMS     1.0000    1.0000    1.0000         2
      PINDFS     0.5000    1.0000    0.6667         1
      PINDMP     1.0000    1.0000    1.0000         1
           X     0.0000    0.0000    0.0000         1
      PINDFP     1.0000    1.0000    1.0000         1

   micro avg     0.9797    0.9797    0.9797     10019
   macro avg     0.9228    0.9230    0.9178     10019
weighted avg     0.9802    0.9797    0.9798     10019
 samples avg     0.9797    0.9797    0.9797     10019
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
