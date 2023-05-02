---
language:
- "zh"
tags:
- "chinese"
- "token-classification"
- "pos"
- "wikipedia"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "apache-2.0"
pipeline_tag: "token-classification"
---

# chinese-roberta-large-upos

## Model Description

This is a BERT model pre-trained on Chinese Wikipedia texts (both simplified and traditional) for POS-tagging and dependency-parsing, derived from [chinese-roberta-wwm-ext-large](https://huggingface.co/hfl/chinese-roberta-wwm-ext-large). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/chinese-roberta-large-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/chinese-roberta-large-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/chinese-roberta-large-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

