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

# deberta-small-coptic-upos

## Model Description

This is a DeBERTa(V2) model pre-trained with [UD_Coptic](https://universaldependencies.org/cop/) for POS-tagging and dependency-parsing, derived from [deberta-small-coptic](https://huggingface.co/KoichiYasuoka/deberta-small-coptic). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-small-coptic-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/deberta-small-coptic-upos")
```

or

```
import esupar
nlp=esupar.load("KoichiYasuoka/deberta-small-coptic-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

