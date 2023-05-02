---
language:
- "be"
tags:
- "belarusian"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
---

# roberta-small-belarusian-upos

## Model Description

This is a RoBERTa model pre-trained with [UD_Belarusian](https://universaldependencies.org/be/) for POS-tagging and dependency-parsing, derived from [roberta-small-belarusian](https://huggingface.co/KoichiYasuoka/roberta-small-belarusian). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-small-belarusian-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-small-belarusian-upos")
```

or

```
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-small-belarusian-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

