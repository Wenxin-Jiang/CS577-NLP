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

# roberta-small-japanese-aozora-char

## Model Description

This is a RoBERTa model pre-trained on 青空文庫 texts with character tokenizer. You can fine-tune `roberta-small-japanese-aozora-char` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-small-japanese-char-luw-upos), dependency-parsing, and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-small-japanese-aozora-char")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-small-japanese-aozora-char")
```

