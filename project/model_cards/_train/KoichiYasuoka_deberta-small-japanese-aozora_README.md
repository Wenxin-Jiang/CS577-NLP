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

# deberta-small-japanese-aozora

## Model Description

This is a DeBERTa(V2) model pre-trained on 青空文庫 texts. NVIDIA A100-SXM4-40GB took 6 hours 42 minutes for training. You can fine-tune `deberta-small-japanese-aozora` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/deberta-small-japanese-luw-upos), dependency-parsing, and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-small-japanese-aozora")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/deberta-small-japanese-aozora")
```

