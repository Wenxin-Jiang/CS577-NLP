---
language:
- "ja"
tags:
- "japanese"
- "masked-lm"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
widget:
- text: "日本に着いたら[MASK]を訪ねなさい。"
---

# roberta-large-japanese-aozora

## Model Description

This is a RoBERTa model pre-trained on 青空文庫 texts with [Japanese-LUW-Tokenizer](https://github.com/KoichiYasuoka/Japanese-LUW-Tokenizer). You can fine-tune `roberta-large-japanese-aozora` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-large-japanese-luw-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-large-japanese-aozora-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-large-japanese-aozora")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-large-japanese-aozora")
```

## Reference

安岡孝一: [Transformersと国語研長単位による日本語係り受け解析モデルの製作](http://id.nii.ac.jp/1001/00216223/), 情報処理学会研究報告, Vol.2022-CH-128, No.7 (2022年2月), pp.1-8.

