---
language:
- "ru"
tags:
- "russian"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
---

# bert-base-russian-upos

## Model Description

This is a BERT model pre-trained with [UD_Russian](https://universaldependencies.org/ru/) for POS-tagging and dependency-parsing, derived from [rubert-base-cased](https://huggingface.co/DeepPavlov/rubert-base-cased). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/bert-base-russian-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/bert-base-russian-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/bert-base-russian-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

