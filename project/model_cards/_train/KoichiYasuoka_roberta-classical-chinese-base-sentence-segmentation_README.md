---
language:
- "lzh"
tags:
- "classical chinese"
- "literary chinese"
- "ancient chinese"
- "sentence segmentation"
- "token-classification"
license: "apache-2.0"
pipeline_tag: "token-classification"
widget:
- text: "子曰學而時習之不亦説乎有朋自遠方來不亦樂乎人不知而不慍不亦君子乎"
---

# roberta-classical-chinese-base-sentence-segmentation

## Model Description

This is a RoBERTa model pre-trained on Classical Chinese texts for sentence segmentation, derived from [roberta-classical-chinese-base-char](https://huggingface.co/KoichiYasuoka/roberta-classical-chinese-base-char). Every segmented sentence begins with token-class "B" and ends with token-class "E" (except for single-character sentence with token-class "S").

## How to Use

```py
import torch
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-classical-chinese-base-sentence-segmentation")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/roberta-classical-chinese-base-sentence-segmentation")
s="子曰學而時習之不亦説乎有朋自遠方來不亦樂乎人不知而不慍不亦君子乎"
p=[model.config.id2label[q] for q in torch.argmax(model(tokenizer.encode(s,return_tensors="pt"))["logits"],dim=2)[0].tolist()[1:-1]]
print("".join(c+"。" if q=="E" or q=="S" else c for c,q in zip(s,p)))
```

## Reference

Koichi Yasuoka: [Sentence Segmentation of Classical Chinese Texts Using Transformers and BERT/RoBERTa Models](http://hdl.handle.net/2433/266539), IPSJ Symposium Series, Vol.2021, No.1 (December 2021), pp.104-109.

