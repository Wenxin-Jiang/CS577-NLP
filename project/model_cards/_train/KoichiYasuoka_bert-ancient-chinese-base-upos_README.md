---
language:
- "lzh"
tags:
- "classical chinese"
- "literary chinese"
- "ancient chinese"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "apache-2.0"
pipeline_tag: "token-classification"
widget:
- text: "子曰學而時習之不亦説乎有朋自遠方來不亦樂乎人不知而不慍不亦君子乎"
---

# bert-ancient-chinese-base-upos

## Model Description

This is a BERT model pre-trained on Classical Chinese texts for POS-tagging and dependency-parsing, derived from [bert-ancient-chinese](https://huggingface.co/Jihuai/bert-ancient-chinese). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech) and [FEATS](https://universaldependencies.org/u/feat/).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/bert-ancient-chinese-base-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/bert-ancient-chinese-base-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/bert-ancient-chinese-base-upos")
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

