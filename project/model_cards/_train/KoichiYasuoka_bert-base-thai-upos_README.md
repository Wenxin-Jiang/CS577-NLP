---
language:
- "th"
tags:
- "thai"
- "token-classification"
- "pos"
- "wikipedia"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "apache-2.0"
pipeline_tag: "token-classification"
widget:
- text: "หลายหัวดีกว่าหัวเดียว"
---

# bert-base-thai-upos

## Model Description

This is a BERT model pre-trained on Thai Wikipedia texts for POS-tagging and dependency-parsing, derived from [bert-base-th-cased](https://huggingface.co/Geotrend/bert-base-th-cased). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/bert-base-thai-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/bert-base-thai-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/bert-base-thai-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

