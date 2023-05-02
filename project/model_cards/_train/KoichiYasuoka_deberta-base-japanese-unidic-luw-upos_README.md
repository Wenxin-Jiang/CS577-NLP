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

# deberta-base-japanese-unidic-luw-upos

## Model Description

This is a DeBERTa(V2) model pre-trained on 青空文庫 texts for POS-tagging and dependency-parsing, derived from [deberta-base-japanese-unidic](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-unidic). Every long-unit-word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech) and [FEATS](https://universaldependencies.org/u/feat/).

## How to Use

```py
import torch
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-base-japanese-unidic-luw-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/deberta-base-japanese-unidic-luw-upos")
s="国境の長いトンネルを抜けると雪国であった。"
t=tokenizer.tokenize(s)
p=[model.config.id2label[q] for q in torch.argmax(model(tokenizer.encode(s,return_tensors="pt"))["logits"],dim=2)[0].tolist()[1:-1]]
print(list(zip(t,p)))
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/deberta-base-japanese-unidic-luw-upos")
print(nlp("国境の長いトンネルを抜けると雪国であった。"))
```

[fugashi](https://pypi.org/project/fugashi), [unidic-lite](https://pypi.org/project/unidic-lite) and [pytokenizations](https://pypi.org/project/pytokenizations) are required.

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

