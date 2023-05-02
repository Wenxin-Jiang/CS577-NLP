---
language:
- "uk"
tags:
- "ukrainian"
- "token-classification"
- "pos"
- "ubertext"
- "dependency-parsing"
datasets:
- "universal_dependencies"
- "ukr-models/Ukr-Synth"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "Свобода і незалежність – найголовніші умови успіху і процвітання."
---

# roberta-base-ukrainian-upos

## Model Description

This is a RoBERTa model pre-trained on Корпус UberText for POS-tagging and dependency-parsing, derived from [roberta-base-ukrainian](https://huggingface.co/KoichiYasuoka/roberta-base-ukrainian). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-ukrainian-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-base-ukrainian-upos")
```

or

```
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-base-ukrainian-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

