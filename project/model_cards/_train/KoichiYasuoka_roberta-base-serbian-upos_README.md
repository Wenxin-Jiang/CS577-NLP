---
language:
- "sr"
tags:
- "serbian"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "Да има сира и масла и моја би мати знала гибати гибаницу."
- text: "Da ima sira i masla i moja bi mati znala gibati gibanicu."
---

# roberta-base-serbian-upos

## Model Description

This is a RoBERTa model in Serbian (Cyrillic and Latin) for POS-tagging and dependency-parsing, derived from [roberta-base-serbian](https://huggingface.co/KoichiYasuoka/roberta-base-serbian). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-serbian-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-base-serbian-upos")
```

or

```
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-base-serbian-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

