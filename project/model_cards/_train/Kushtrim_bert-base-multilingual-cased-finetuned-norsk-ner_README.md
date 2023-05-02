---
language:
- no
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikiann
model-index:
- name: bert-base-multilingual-cased-finetuned-norsk-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-norsk-ner

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the wikiann dataset.

### Usage
```python
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("Kushtrim/bert-base-multilingual-cased-finetuned-norsk-ner")

model = AutoModelForTokenClassification.from_pretrained("Kushtrim/bert-base-multilingual-cased-finetuned-norsk-ner")
ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy='first')

text = "Sett inn tekst her"

results = ner(text)

pd.DataFrame.from_records(results)
```
