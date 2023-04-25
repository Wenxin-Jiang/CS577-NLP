---
language: 
  - grc
tags:
  - flair
  - token-classification
widget:
  - ταῦτα εἴπας ὁ Ἀλέξανδρος παρίζει Πέρσῃ ἀνδρὶ ἄνδρα Μακεδόνα ὡς γυναῖκα τῷ λόγῳ · οἳ δέ , ἐπείτε σφέων οἱ Πέρσαι ψαύειν ἐπειρῶντο , διεργάζοντο αὐτούς .
---
# Named Entity Recognition for Ancient Greek 

Pretrained NER tagging model for ancient Greek

# Scores & Tagset
<details> 

### Training:
|      | Precision | Recall   | F1-score | Support|
|------|:---------:|:--------:|:--------:|:--------:|
|PER  |   91.24%  |   94.45%  |   92.82%    |   2127|
|MISC |   80.92%  |   83.17%  |   82.03%    |    933|
|LOC  |   86.86%  |   78.35%  |   82.38%    |    388|

### Evaluation
|      | Precision | Recall   | F1-score |Support|
|------|:---------:|:--------:|:--------:|:--------:|
| PER  |   92.00%  |  86.79%  |  89.32%  |  124|
| MISC |   96.43%  |  87.10%  |  91.53%  |  159|
| LOC  |   80.00%  |  84.85%  |  82.35%  |  66|

</details>

- F-score (micro) 0.8878
- F-score (macro) 0.8574
- Accuracy 0.8324

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
