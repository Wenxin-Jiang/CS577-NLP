---
language: de
tags:
- pytorch
- tf
- bert
- NER
datasets:
- legal entity recognition

---

### NER model trained on BERT 

MODEL used for fine tuning is GBERT Large by deepset.ai



## Test
Accuracy: 98 \
F1: 84.1 \
Precision: 82.7 \
Recall: 85.5

## Model inferencing:
```python
!pip install -q transformers
from transformers import pipeline

ner = pipeline(
    "ner",
    model="Sahajtomar/NER_legal_de",
    tokenizer="Sahajtomar/NER_legal_de")
    
 nlp_ner("Für eine Zuständigkeit des Verwaltungsgerichts Berlin nach § 52 Nr. 1 bis 4 VwGO hat der \
         Antragsteller keine Anhaltspunkte vorgetragen .")
         
```
