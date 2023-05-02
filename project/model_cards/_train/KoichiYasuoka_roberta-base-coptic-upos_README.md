---
language:
- "cop"
tags:
- "coptic"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "ⲧⲉⲛⲟⲩⲇⲉⲛ̄ⲟⲩⲟⲉⲓⲛϩ︤ⲙ︥ⲡϫⲟⲉⲓⲥ·"
- text: "ⲙⲟⲟϣⲉϩⲱⲥϣⲏⲣⲉⲙ̄ⲡⲟⲩⲟⲉⲓⲛ·"
---

# roberta-base-coptic-upos

## Model Description

This is a RoBERTa model pre-trained with [UD_Coptic](https://universaldependencies.org/cop/) for POS-tagging and dependency-parsing, derived from [roberta-base-coptic](https://huggingface.co/KoichiYasuoka/roberta-base-coptic). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-coptic-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-base-coptic-upos")
```

or

```
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-base-coptic-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

