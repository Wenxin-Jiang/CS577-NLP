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

# deberta-base-thai-upos

## Model Description

This is a DeBERTa(V2) model pre-trained on Thai Wikipedia texts for POS-tagging and dependency-parsing, derived from [deberta-base-thai](https://huggingface.co/KoichiYasuoka/deberta-base-thai). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
import torch
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-base-thai-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/deberta-base-thai-upos")
s="หลายหัวดีกว่าหัวเดียว"
t=tokenizer.tokenize(s)
p=[model.config.id2label[q] for q in torch.argmax(model(tokenizer.encode(s,return_tensors="pt"))["logits"],dim=2)[0].tolist()[1:-1]]
print(list(zip(t,p)))
```

or

```
import esupar
nlp=esupar.load("KoichiYasuoka/deberta-base-thai-upos")
print(nlp("หลายหัวดีกว่าหัวเดียว"))
```

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

