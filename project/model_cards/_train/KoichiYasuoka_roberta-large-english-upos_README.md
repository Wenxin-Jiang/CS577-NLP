---
language:
- "en"
tags:
- "english"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
---

# roberta-large-english-upos

## Model Description

This is a RoBERTa model pre-trained with [UD_English](https://universaldependencies.org/en/) for POS-tagging and dependency-parsing, derived from [roberta-large](https://huggingface.co/roberta-large). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-large-english-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-large-english-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-large-english-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

