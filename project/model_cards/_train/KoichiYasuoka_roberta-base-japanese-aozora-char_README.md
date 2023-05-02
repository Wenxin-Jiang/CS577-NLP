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

# roberta-base-japanese-aozora-char

## Model Description

This is a RoBERTa model pre-trained on 青空文庫 texts with character tokenizer. You can fine-tune `roberta-base-japanese-aozora-char` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-japanese-char-luw-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-base-japanese-aozora-ud-head), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-japanese-aozora-char")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-japanese-aozora-char")
```

## Reference

安岡孝一: [Transformersと国語研長単位による日本語係り受け解析モデルの製作](http://id.nii.ac.jp/1001/00216223/), 情報処理学会研究報告, Vol.2022-CH-128, No.7 (2022年2月), pp.1-8.

