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
license: "apache-2.0"
pipeline_tag: "token-classification"
---

# deberta-base-chinese-erlangshen-upos

## Model Description

This is a DeBERTa(V2) model pre-trained on Chinese texts (both simplified and traditional) for POS-tagging and dependency-parsing, derived from [Erlangshen-DeBERTa-v2-97M-Chinese](https://huggingface.co/IDEA-CCNL/Erlangshen-DeBERTa-v2-97M-Chinese). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-base-chinese-erlangshen-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/deberta-base-chinese-erlangshen-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/deberta-base-chinese-erlangshen-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

