---
language:
- "be"
- "bg"
- "mk"
- "ru"
- "sr"
- "uk"
tags:
- "belarusian"
- "bulgarian"
- "macedonian"
- "russian"
- "serbian"
- "ukrainian"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
---

# bert-base-slavic-cyrillic-upos

## Model Description

This is a BERT model pre-trained with Slavic-Cyrillic ([UD_Belarusian](https://universaldependencies.org/be/) [UD_Bulgarian](https://universaldependencies.org/bg/) [UD_Russian](https://universaldependencies.org/ru/) [UD_Serbian](https://universaldependencies.org/treebanks/sr_set/) [UD_Ukrainian](https://universaldependencies.org/treebanks/uk_iu/)) for POS-tagging and dependency-parsing, derived from [ruBert-base](https://huggingface.co/sberbank-ai/ruBert-base). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/bert-base-slavic-cyrillic-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/bert-base-slavic-cyrillic-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/bert-base-slavic-cyrillic-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

