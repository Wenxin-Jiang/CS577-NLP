---
language:
- "vi"
tags:
- "vietnamese"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "Hai cái đầu thì tốt hơn một."
---

# roberta-base-vietnamese-upos

## Model Description

This is a RoBERTa model pre-trained on Vietnamese texts for POS-tagging and dependency-parsing, derived from [roberta-base-vietnamese](https://huggingface.co/KoichiYasuoka/roberta-base-vietnamese). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/)(Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification,TokenClassificationPipeline
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-vietnamese-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-base-vietnamese-upos")
pipeline=TokenClassificationPipeline(tokenizer=tokenizer,model=model,aggregation_strategy="simple")
nlp=lambda x:[(x[t["start"]:t["end"]],t["entity_group"]) for t in pipeline(x)]
print(nlp("Hai cái đầu thì tốt hơn một."))
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-base-vietnamese-upos")
print(nlp("Hai cái đầu thì tốt hơn một."))
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models
