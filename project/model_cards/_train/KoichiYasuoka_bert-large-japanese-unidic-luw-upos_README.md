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

# bert-large-japanese-unidic-luw-upos

## Model Description

This is a BERT model pre-trained on Japanese Wikipedia texts for POS-tagging and dependency-parsing, derived from [bert-large-japanese](https://huggingface.co/cl-tohoku/bert-large-japanese). Every long-unit-word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
import torch
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/bert-large-japanese-unidic-luw-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/bert-large-japanese-unidic-luw-upos")
s="国境の長いトンネルを抜けると雪国であった。"
t=tokenizer.tokenize(s)
p=[model.config.id2label[q] for q in torch.argmax(model(tokenizer.encode(s,return_tensors="pt"))["logits"],dim=2)[0].tolist()[1:-1]]
print(list(zip(t,p)))
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/bert-large-japanese-unidic-luw-upos")
print(nlp("国境の長いトンネルを抜けると雪国であった。"))
```

[fugashi](https://pypi.org/project/fugashi), [unidic-lite](https://pypi.org/project/unidic-lite) and [pytokenizations](https://pypi.org/project/pytokenizations) are required.

## Reference

安岡孝一: [Transformersと国語研長単位による日本語係り受け解析モデルの製作](http://id.nii.ac.jp/1001/00216223/), 情報処理学会研究報告, Vol.2022-CH-128, No.7 (2022年2月), pp.1-8.

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

