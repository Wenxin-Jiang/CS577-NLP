---
language: no
license: cc-by-4.0
tags:
- norwegian
- bert
- ner
thumbnail: nblogo_3.png
pipeline_tag: token-classification
datasets:
- norne
inference:
  parameters:
    aggregation_strategy: "first"
widget:
- text: Trond Giske har bekreftet på spørsmål fra Adresseavisen at Hansen leide et rom i hans leilighet i Trondheim.
---

**Release 1.0** (November 17, 2021)

# nb-bert-base-ner

## Description
NB-Bert base model fine-tuned on the Named Entity Recognition task using the [NorNE dataset](https://huggingface.co/datasets/NbAiLab/norne).

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("NbAiLab/nb-bert-base-ner")
model = AutoModelForTokenClassification.from_pretrained("NbAiLab/nb-bert-base-ner")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Jeg heter Kjell og bor i Oslo."

ner_results = nlp(example)
print(ner_results)
```