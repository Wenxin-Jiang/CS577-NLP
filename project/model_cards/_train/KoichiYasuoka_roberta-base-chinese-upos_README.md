---
language:
- "zh"
tags:
- "chinese"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
---

# roberta-base-chinese-upos

## Model Description

This is a RoBERTa model pre-trained on Chinese Wikipedia texts (both simplified and traditional) for POS-tagging and dependency-parsing, derived from [roberta-base-chinese](https://huggingface.co/KoichiYasuoka/roberta-base-chinese). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-chinese-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-base-chinese-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-base-chinese-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

