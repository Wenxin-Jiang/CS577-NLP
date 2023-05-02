---
language:
- "ja"
tags:
- "japanese"
- "token-classification"
- "pos"
- "wikipedia"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "国境の長いトンネルを抜けると雪国であった。"
---

# bert-large-japanese-upos

## Model Description

This is a BERT model pre-trained on Japanese Wikipedia texts for POS-tagging and dependency-parsing, derived from [bert-large-japanese-char-extended](https://huggingface.co/KoichiYasuoka/bert-large-japanese-char-extended). Every short-unit-word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
import torch
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/bert-large-japanese-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/bert-large-japanese-upos")
s="国境の長いトンネルを抜けると雪国であった。"
p=[model.config.id2label[q] for q in torch.argmax(model(tokenizer.encode(s,return_tensors="pt"))["logits"],dim=2)[0].tolist()[1:-1]]
print(list(zip(s,p)))
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/bert-large-japanese-upos")
print(nlp("国境の長いトンネルを抜けると雪国であった。"))
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

