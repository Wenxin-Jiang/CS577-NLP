---
language:
- "ja"
tags:
- "japanese"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "国境の長いトンネルを抜けると雪国であった。"
---

# roberta-large-japanese-luw-upos

## Model Description

This is a RoBERTa model pre-trained on 青空文庫 texts for POS-tagging and dependency-parsing, derived from [roberta-large-japanese-aozora](https://huggingface.co/KoichiYasuoka/roberta-large-japanese-aozora). Every long-unit-word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification,TokenClassificationPipeline
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-large-japanese-luw-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-large-japanese-luw-upos")
pipeline=TokenClassificationPipeline(tokenizer=tokenizer,model=model,aggregation_strategy="simple")
nlp=lambda x:[(x[t["start"]:t["end"]],t["entity_group"]) for t in pipeline(x)]
print(nlp("国境の長いトンネルを抜けると雪国であった。"))
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-large-japanese-luw-upos")
print(nlp("国境の長いトンネルを抜けると雪国であった。"))
```

## Reference

安岡孝一: [Transformersと国語研長単位による日本語係り受け解析モデルの製作](http://id.nii.ac.jp/1001/00216223/), 情報処理学会研究報告, Vol.2022-CH-128, No.7 (2022年2月), pp.1-8.

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

