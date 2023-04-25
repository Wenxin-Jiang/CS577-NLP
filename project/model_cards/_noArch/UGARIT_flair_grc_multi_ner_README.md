---
language: 
  - grc
tags:
  - flair
  - token-classification
  - ner
widget:
  - ταῦτα εἴπας ὁ Ἀλέξανδρος παρίζει Πέρσῃ ἀνδρὶ ἄνδρα Μακεδόνα ὡς γυναῖκα τῷ λόγῳ · οἳ δέ , ἐπείτε σφέων οἱ Πέρσαι ψαύειν ἐπειρῶντο , διεργάζοντο αὐτούς .
---
# Named Entity Recognition for Ancient Greek 

Pretrained NER tagging model for ancient Greek

# Scores & Tagset
<details> 

### Training
|      | Precision | Recall   | F1-score | Support |
|------|:---------:|:--------:|:--------:|:-------:|
| PER  |   93.39%  |  96.33%  |  94.84%  |   2127  |
| MISC |   84.69%  |  92.50%  |  88.42%  |   933   |
| LOC  |   89.55%  |  77.32%  |  82.99%  |   388   |

### Evaluation

|      | Precision | Recall   | F1-score | Support |
|------|:---------:|:--------:|:--------:|:-------:|
| PER  |   90.48%  |  91.94%  |  91.20%  |   124   |
| MISC |   89.29%  |  94.34%  |  91.74%  |   159   |
| LOC  |   82.69%  |  65.15%  |  72.88%  |    66   |

</details>


# Usage
```python
from flair.data import Sentence
from flair.models import SequenceTagger
  
tagger = SequenceTagger.load("UGARIT/flair_grc_bert_ner")
sentence = Sentence('ταῦτα εἴπας ὁ Ἀλέξανδρος παρίζει Πέρσῃ ἀνδρὶ ἄνδρα Μακεδόνα ὡς γυναῖκα τῷ λόγῳ · οἳ δέ , ἐπείτε σφέων οἱ Πέρσαι ψαύειν ἐπειρῶντο , διεργάζοντο αὐτούς .')
tagger.predict(sentence)
for entity in sentence.get_spans('ner'):
    print(entity)
```


 # Citation
*if you use this model, please consider citing [this work](https://www.researchgate.net/publication/365131651_Transformer-Based_Named_Entity_Recognition_for_Ancient_Greek):*
```latex
@unpublished{yousefetal22
author = "Yousef, Tariq and Palladino, Chiara and Jänicke, Stefan",
title = "Transformer-Based Named Entity Recognition for Ancient Greek",
year = {2022},
month = {11},
doi = "10.13140/RG.2.2.34846.61761"
url = {https://www.researchgate.net/publication/358956953_Sequence_Labeling_Architectures_in_Diglossia_-_a_case_study_of_Arabic_and_its_dialects}
}
