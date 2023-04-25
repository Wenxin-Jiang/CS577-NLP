---
language: 
- ar
- en
license: apache-2.0
datasets:
- 4Dialects
- MADAR
- CSCS
thumbnail: https://www.informatik.hu-berlin.de/en/forschung-en/gebiete/ml-en/resolveuid/a6f82e0d7fa446a59c902cac4cafa9cb/@@images/image/preview
tags:
- flair
- token-classification
- sequence-tagger-model
- Dialectal Arabic
- Code-Switching
- Code-Mixing
metrics:
- f1
widget:
- text: "طلعوا جماعة الممانعة بالسياسة ما بيعرفوا ولا بالصحة بيعرفوا ولا حتى بالدين"
- text: "أعلم أن هذا يبدو غير عادل ، لكن لا يمكن أن يكون هناك ظلم"
- text: "أنا عارف أن الموضوع ده شكله مش عادل ، بس لا يمكن أن يكون فيه ظلم"
---


# Arabic Flair + fastText Part-of-Speech tagging Model (Egyptian and Levant)
Pretrained Part-of-Speech tagging model built on a joint corpus written in Egyptian and Levantine (Jordanian, Lebanese, Palestinian, Syrian) dialects with code-switching of Egyptian Arabic and English. The model is trained using [Flair](https://aclanthology.org/C18-1139/) (forward+backward)and [fastText](https://fasttext.cc) embeddings.



# Pretraining Corpora:
This sequence labeling model was pretrained on three corpora jointly:
1. [4 Dialects](https://huggingface.co/datasets/viewer/?dataset=arabic_pos_dialect)
A Dialectal Arabic Datasets containing four dialects of Arabic, Egyptian (EGY), Levantine (LEV), Gulf (GLF), and Maghrebi (MGR). Each dataset consists of a set of 350 manually segmented and PoS tagged tweets.
2. [UD South Levantine Arabic MADAR](https://universaldependencies.org/treebanks/ajp_madar/index.html)
A Dataset with 100 manually-annotated sentences taken from the [MADAR](https://camel.abudhabi.nyu.edu/madar/) (Multi-Arabic Dialect Applications and Resources) project by [Shorouq Zahra](mailto:shorouqjzahra@gmail.com).
3. Parts of the Cairo Students Code-Switch (CSCS) corpus developed for ["Collection and Analysis of Code-switch Egyptian Arabic-English Speech Corpus"](https://aclanthology.org/L18-1601.pdf) by Hamed et al.

# Usage
```python
from flair.data import Sentence
from flair.models import SequenceTagger
  
tagger = SequenceTagger.load("megantosh/flair-arabic-dialects-codeswitch-egy-lev")
sentence = Sentence('عمرو عادلي أستاذ للاقتصاد السياسي المساعد في الجامعة الأمريكية  بالقاهرة .')
tagger.predict(sentence)
for entity in sentence.get_spans('pos'):
    print(entity)
```

Due to the right-to-left in left-to-right context, some formatting errors might occur. and your code might appear like [this](https://ibb.co/ky20Lnq), (link accessed on 2020-10-27) 

<!--# Example

# Tagset-->

# Scores & Tagset
<details> 

| |precision |   recall | f1-score |  support|
|--|-----------|------|-------------|--------------|
|INTJ |    0.8182   | 0.9000    |0.8571    |    10|
|OUN   |  0.9009   | 0.9402    |0.9201      | 435|
|NUM    | 0.9524   | 0.8333   | 0.8889       | 24|
|ADJ     |0.8762   | 0.7603  |  0.8142      | 121|
|ADP     |0.9903    |0.9623 |   0.9761       |106|
| CCONJ |    0.9600   | 0.9730 |   0.9664 |       74|
|PROPN |    0.9333   | 0.9333  |  0.9333  |      15|
| ADV  |   0.9135   | 0.8051  |  0.8559   |    118|
|VERB   |  0.8852    | 0.9231 |   0.9038   |    117|
|PRON    | 0.9620    | 0.9465 |   0.9542    |   187|
|SCONJ |    0.8571   | 0.9474  |  0.9000      |  19|
|PART  |   0.9350   | 0.9791   | 0.9565       | 191|
| DET   |  0.9348    | 0.9149  |  0.9247 |       47|
|PUNCT    | 1.0000    | 1.0000  |  1.0000  |      35|
| AUX  |   0.9286    | 0.9811  |  0.9541   |     53|
|MENTION   |  0.9231   |  1.0000  |  0.9600    |    12|
|     V    | 0.8571   | 0.8780    | 0.8675     |   82|
| FUT-PART+V+PREP+PRON     |1.0000   | 0.0000   | 0.0000       |  1|
|  PROG-PART+V+PRON+PREP+PRON |     0.0000  |  1.0000  |  0.0000       |  0|
|ADJ+NSUFF |    0.6111   | 0.8462   | 0.7097 |       26|
|NOUN+NSUFF  |   0.8182   | 0.8438   | 0.8308  |      64|
|PREP+PRON   |  0.9565   | 0.9565   | 0.9565   |     23|
|                   PUNC    | 0.9941   | 1.0000   | 0.9971    |   169|
|                    EOS     |1.0000   | 1.0000   | 1.0000    |   70|
|             NOUN+PRON   |  0.6986   | 0.8500   | 0.7669      |  60|
|                V+PRON    | 0.7258   | 0.8036   | 0.7627       | 56|
|            PART+PRON    | 1.0000   | 0.9474   | 0.9730    |    19|
|          PROG-PART+V    | 0.8333   | 0.9302   | 0.8791 |       43|
|            DET+NOUN    | 0.9625   | 1.0000   | 0.9809  |      77|
|     NOUN+NSUFF+PRON    | 0.9091   | 0.7143   | 0.8000   |     14|
|     PROG-PART+V+PRON    | 0.7083   | 0.9444   | 0.8095    |    18|
|      PREP+NOUN+NSUFF    | 0.6667   | 0.4000   | 0.5000         5|
|     NOUN+NSUFF+NSUFF    | 1.0000   | 0.0000   | 0.0000 |        3|
|                CONJ    | 0.9722   | 1.0000   | 0.9859  |      35|
|        V+PRON+PRON    | 0.6364   | 0.5833   | 0.6087   |     12|
|           FOREIGN    | 0.6667   | 0.6667   | 0.6667    |     3|
|        PREP+NOUN    | 0.6316   | 0.7500  |  0.6857 |       16|
|  DET+NOUN+NSUFF    | 0.9000   | 0.9310  |  0.9153  |      29|
|  DET+ADJ+NSUFF    | 1.0000   | 0.5714  |  0.7273   |      7|
|     CONJ+PRON    | 1.0000   | 0.8750  |  0.9333     |    8|
|    NOUN+CASE    | 0.0000   | 0.0000  |  0.0000    |     2|
|     DET+ADJ    | 1.0000   | 0.6667  |  0.8000      |   6|
|       PREP    | 1.0000   | 0.9718  |  0.9857  |      71|
|  CONJ+FUT-PART+V    | 0.0000   | 0.0000  |  0.0000   |      1|
|            CONJ+V    | 0.6667   | 0.7500  |  0.7059    |     8|
|         FUT-PART    | 1.0000   | 1.0000  |  1.0000     |    2|
|             ADJ+PRON    | 1.0000   | 0.0000  |  0.0000      |   8|
|   CONJ+PREP+NOUN+PRON    | 1.0000   | 0.0000  |  0.0000       |  1|
|        CONJ+NOUN+PRON    | 0.3750   | 1.0000  |  0.5455      |   3|
|              PART+ADJ    | 1.0000   | 0.0000  |  0.0000       |  1|
|             PART+NOUN    | 0.5000   | 1.0000  |  0.6667        | 1|
|       CONJ+PREP+NOUN    | 1.0000   | 0.0000  |  0.0000       |  1|
|           CONJ+NOUN    | 0.7000   | 0.7778  |  0.7368  |       9|
|                URL    | 1.0000   | 1.0000   | 1.0000 |        3|
|     CONJ+FUT-PART    | 1.0000   | 0.0000   | 0.0000  |       1|
|       FUT-PART+V    | 0.8571   | 0.6000   | 0.7059   |     10|
|      PREP+NOUN+NSUFF+NSUFF    | 1.0000   | 0.0000    | 0.0000   |      1|
|                      HASH    | 1.0000   | 0.9412   | 0.9697     |   17|
|            ADJ+PREP+PRON    | 1.0000   | 0.0000   | 0.0000  |       3|
|          PREP+NOUN+PRON    | 0.0000   | 0.0000   | 0.0000   |      1|
|                   EMOT    | 1.0000   | 0.8889   | 0.9412    |    18|
|             CONJ+PREP    | 1.0000   | 0.7500   | 0.8571     |    4|
|  PREP+DET+NOUN+NSUFF    | 1.0000   | 0.7500   | 0.8571      |   4|
| PRON+DET+NOUN+NSUFF    | 0.0000   | 1.0000   | 0.0000       |  0|
|        V+PREP+PRON    | 1.0000   | 0.0000   | 0.0000        | 5|
|  V+PRON+PREP+PRON    | 0.0000   | 1.0000   | 0.0000         | 0|
|  CONJ+NOUN+NSUFF    | 0.5000   | 0.5000   | 0.5000 |        2|
|      V+NEG-PART    | 1.0000   | 0.0000   | 0.0000  |       2|
|  PREP+DET+NOUN    | 0.9091   | 1.0000   | 0.9524   |     10|
|        PREP+V    | 1.0000   | 0.0000   | 0.0000    |     2|
|    CONJ+PART    | 1.0000   | 0.7778   | 0.8750     |    9|
| CONJ+V+PRON    | 1.0000   | 1.0000   | 1.0000 |        5|
|    PROG-PART+V+PREP+PRON    | 1.0000   | 0.5000   | 0.6667  |       2|
|    PREP+NOUN+NSUFF+PRON    | 1.0000   | 1.0000   | 1.0000   |      1|
|               ADJ+CASE    | 1.0000   | 0.0000    | 0.0000   |      1|
|        PART+NOUN+PRON    | 1.0000   | 1.0000   | 1.0000     |    1|
|               PART+V    | 1.0000   | 0.0000  |  0.0000      |   3|
|         PART+V+PRON    | 0.0000   | 1.0000  |  0.0000       |  0|
|    FUT-PART+V+PRON    | 0.0000   | 1.0000  |  0.0000        | 0|
|FUT-PART+V+PRON+PRON    | 1.0000   | 0.0000  |  0.0000  |       1|
|     CONJ+PREP+PRON    | 1.0000   | 0.0000  |  0.0000   |      1|
|CONJ+V+PRON+PREP+PRON    | 1.0000   | 0.0000  |  0.0000    |     1|
|    CONJ+V+PREP+PRON    | 0.0000   | 1.0000  |  0.0000     |    0|
|CONJ+DET+NOUN+NSUFF    | 1.0000   | 0.0000  |  0.0000      |   1|
|     CONJ+DET+NOUN    | 0.6667   | 1.0000  |  0.8000    |     2|
| CONJ+PREP+DET+NOUN   |  1.0000  |  1.0000 |   1.0000  |       1|
|       PREP+PART    | 1.0000   | 0.0000  |  0.0000  |       2|
|      PART+V+PRON+NEG-PART    | 0.3333   | 0.3333  |  0.3333         | 3|
|          PART+V+NEG-PART    | 0.3333   | 0.5000  |  0.4000        | 2|
|      PART+PREP+NEG-PART    | 1.0000   | 1.0000  |  1.0000       |  3|
| PART+PROG-PART+V+NEG-PART    | 1.0000   | 0.3333   | 0.5000      |   3|
| PREP+DET+NOUN+NSUFF+PREP+PRON   |  1.0000  |  0.0000  |  0.0000    |     1|
|         PREP+PRON+DET+NOUN    | 0.0000   | 1.0000    | 0.0000   |      0|
|                PART+NSUFF    | 1.0000   | 0.0000    | 0.0000  |       1|
|    CONJ+PROG-PART+V+PRON    | 1.0000   | 1.0000   | 1.0000    |     1|
|          PART+PREP+PRON    | 1.0000   | 0.0000   | 0.0000   |      1|
|         CONJ+PART+PREP    | 1.0000   | 0.0000    | 0.0000        | 1|
|             NUM+NSUFF    | 0.6667   | 0.6667   | 0.6667        | 3|
| CONJ+PART+V+PRON+NEG-PART   |  1.0000  |  1.0000  |  1.0000      |   1|
|     PART+NOUN+NEG-PART    | 1.0000   | 1.0000   | 1.0000      |   1|
|        CONJ+ADJ+NSUFF     | 1.0000  |  0.0000  |  0.0000    |     1|
|             PREP+ADJ     | 1.0000  |  0.0000  |  0.0000   |      1|
|      ADJ+NSUFF+PRON     | 1.0000  |  0.0000  |  0.0000  |       2|
|   CONJ+PROG-PART+V    | 1.0000   | 0.0000   | 0.0000   |      1|
| CONJ+PART+PROG-PART+V+PREP+PRON+NEG-PART   |  1.0000  |  0.0000  |  0.0000 |        1|
|          CONJ+PART+PREP+PRON+NEG-PART    | 0.0000   | 1.0000   | 0.0000 |        0|
|                       PREP+PART+PRON    | 1.0000   | 0.0000   | 0.0000    |     1|
|                      CONJ+ADV+NSUFF    | 1.0000   | 0.0000    |0.0000   |      1|
|                           CONJ+ADV    | 0.0000   | 1.0000   | 0.0000  |       0|
|           PART+NOUN+PRON+NEG-PART    | 0.0000   | 1.0000  |  0.0000 |        0|
|                         CONJ+ADJ    | 1.0000   | 1.0000 |   1.0000 |         1|

</details>

- F-score (micro): 0.8974
- F-score (macro): 0.5188
- Accuracy (incl. no class): 0.901  

Expand details below to show class scores for each tag. Note that tag compounds (a tag made for multiple agglutinated parts of speech) are considered as separate ones.

 # Citation
*if you use this model, please consider citing [this work](https://www.researchgate.net/publication/358956953_Sequence_Labeling_Architectures_in_Diglossia_-_a_case_study_of_Arabic_and_its_dialects):*
```latex
@unpublished{MMHU21
author = "M. Megahed",
title = "Sequence Labeling Architectures in Diglossia",
year = {2021},
doi = "10.13140/RG.2.2.34961.10084"
url = {https://www.researchgate.net/publication/358956953_Sequence_Labeling_Architectures_in_Diglossia_-_a_case_study_of_Arabic_and_its_dialects}
}
```