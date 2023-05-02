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

# roberta-base-thai-char-upos

## Model Description

This is a RoBERTa model pre-trained on Thai Wikipedia texts for POS-tagging and dependency-parsing, derived from [roberta-base-thai-char](https://huggingface.co/KoichiYasuoka/roberta-base-thai-char). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
import torch
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-thai-char-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-base-thai-char-upos")
s="หลายหัวดีกว่าหัวเดียว"
t=tokenizer.tokenize(s)
p=[model.config.id2label[q] for q in torch.argmax(model(tokenizer.encode(s,return_tensors="pt"))["logits"],dim=2)[0].tolist()[1:-1]]
print(list(zip(t,p)))
```

or

```
import esupar
nlp=esupar.load("KoichiYasuoka/roberta-base-thai-char-upos")
print(nlp("หลายหัวดีกว่าหัวเดียว"))
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

