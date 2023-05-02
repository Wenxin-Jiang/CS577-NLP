---
language:
- "ko"
tags:
- "korean"
- "token-classification"
- "pos"
- "dependency-parsing"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "홍시 맛이 나서 홍시라 생각한다."
- text: "紅柹 맛이 나서 紅柹라 生覺한다."
---

# roberta-large-korean-morph-upos

## Model Description

This is a RoBERTa model pre-trained on Korean texts for POS-tagging and dependency-parsing, derived from [roberta-large-korean-hanja](https://huggingface.co/KoichiYasuoka/roberta-large-korean-hanja) and [morphUD-korean](https://github.com/jungyeul/morphUD-korean). Every morpheme (형태소) is tagged by [UPOS](https://universaldependencies.org/u/pos/)(Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification,TokenClassificationPipeline
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-large-korean-morph-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-large-korean-morph-upos")
pipeline=TokenClassificationPipeline(tokenizer=tokenizer,model=model,aggregation_strategy="simple")
nlp=lambda x:[(x[t["start"]:t["end"]],t["entity_group"]) for t in pipeline(x)]
print(nlp("홍시 맛이 나서 홍시라 생각한다."))
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-large-korean-morph-upos")
print(nlp("홍시 맛이 나서 홍시라 생각한다."))
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models
