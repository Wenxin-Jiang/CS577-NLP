---
language: 
- multilingual
- ar 
- cs
- de
- en
- es
- et
- fi
- fr
- gu
- hi
- it
- ja
- kk
- ko
- lt
- lv
- my
- ne
- nl
- ro
- ru
- si
- tr
- vi
- zh
- af
- az
- bn
- fa
- he
- hr
- id
- ka
- km
- mk
- ml
- mn
- mr
- pl
- ps
- pt
- sv
- sw
- ta
- te
- th
- tl
- uk
- ur
- xh
- gl
- sl
license: mit
tags:
- mbart-50
---

# Knight-errant

Knight is a text style transfer model for knight-errant style. This model is for Chinese Knight-errant style transfer.

paper link: [To be a Knight-errant Novel Master: Knight-errant Style Transfer via Contrastive Learning](https://openreview.net/forum?id=FDw2hdpiWNO)


```python

#inference
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("Anonymous-TST/knight-errant-TST-zh")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50", src_lang="zh_CN", tgt_lang="zh_CN")

model.cuda()
model.eval()

article_1 = "jinyong: 接下来会发生什么？"
batch = tokenizer(article_1, return_tensors="pt",return_token_type_ids=False, truncation=True, max_length=64, padding=True).to('cuda')
translated_tokens = model.generate(**batch,max_length=64)
decoded = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True,  clean_up_tokenization_spaces=True)
print(decoded)
# 欲知后事如何?
```




```