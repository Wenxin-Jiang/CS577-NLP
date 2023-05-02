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

# roberta-classical-chinese-large-upos

## Model Description

This is a RoBERTa model pre-trained on Classical Chinese texts for POS-tagging and dependency-parsing, derived from [roberta-classical-chinese-large-char](https://huggingface.co/KoichiYasuoka/roberta-classical-chinese-large-char). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech) and [FEATS](https://universaldependencies.org/u/feat/).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-classical-chinese-large-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-classical-chinese-large-upos")
```
or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-classical-chinese-large-upos")
```

## Reference

Koichi Yasuoka: [Universal Dependencies Treebank of the Four Books in Classical Chinese](http://hdl.handle.net/2433/245217), DADH2019: 10th International Conference of Digital Archives and Digital Humanities (December 2019), pp.20-28.

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

