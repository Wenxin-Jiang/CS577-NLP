---
tags:
- bert
- token-classification
- sequence-tagger-model
language: en
widget:
- text: "Total exports of maize"
---

## Token Classification
Classifies Gro's items and metrics

| **tag**                        | **token** |
|---------------------------------|-----------|
|B-ITEM    | BEGINNING ITEM|
|I-ITEM    | INSIDE ITEM|
|B-METRIC   |BEGINNING METRIC  |
|I-METRIC    | INSIDE METRIC|
|O          | OUTSIDE |

---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline
tokenizer = AutoTokenizer.from_pretrained("Wanjiru/autotrain_gro_ner")

model = AutoModelForTokenClassification.from_pretrained("Wanjiru/autotrain_gro_ner")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Wanjru"
ner_res = nlp(example)
  
```



---
