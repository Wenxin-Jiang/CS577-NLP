---
language:
- "de"
tags:
- "german"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "mit"
pipeline_tag: "token-classification"
---

# bert-large-german-upos

## Model Description

This is a BERT model pre-trained with [UD_German-HDT](https://github.com/UniversalDependencies/UD_German-HDT) for POS-tagging and dependency-parsing, derived from [gbert-large](https://huggingface.co/deepset/gbert-large). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/bert-large-german-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/bert-large-german-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/bert-large-german-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

