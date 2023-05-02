---
language:
- "ja"
tags:
- "japanese"
- "wikipedia"
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

# deberta-large-japanese-wikipedia-luw-upos

## Model Description

This is a DeBERTa(V2) model pre-trained on Japanese Wikipedia and 青空文庫 texts for POS-tagging and dependency-parsing, derived from [deberta-large-japanese-wikipedia](https://huggingface.co/KoichiYasuoka/deberta-large-japanese-wikipedia). Every long-unit-word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech) and [FEATS](https://universaldependencies.org/u/feat/).

## How to Use

```py
import torch
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-large-japanese-wikipedia-luw-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/deberta-large-japanese-wikipedia-luw-upos")
s="国境の長いトンネルを抜けると雪国であった。"
t=tokenizer.tokenize(s)
p=[model.config.id2label[q] for q in torch.argmax(model(tokenizer.encode(s,return_tensors="pt"))["logits"],dim=2)[0].tolist()[1:-1]]
print(list(zip(t,p)))
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/deberta-large-japanese-wikipedia-luw-upos")
print(nlp("国境の長いトンネルを抜けると雪国であった。"))
```

## Reference

安岡孝一: [青空文庫DeBERTaモデルによる国語研長単位係り受け解析](http://hdl.handle.net/2433/275409), 東洋学へのコンピュータ利用, 第35回研究セミナー (2022年7月), pp.29-43.

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

