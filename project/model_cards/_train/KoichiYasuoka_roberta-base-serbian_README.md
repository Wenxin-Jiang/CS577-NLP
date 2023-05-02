---
language:
- "sr"
tags:
- "serbian"
- "masked-lm"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# roberta-base-serbian

## Model Description

This is a RoBERTa model in Serbian (Cyrillic and Latin) pre-trained on [srWaC](http://hdl.handle.net/11356/1063). You can fine-tune `roberta-base-serbian` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-serbian-upos), dependency-parsing, and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-serbian")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-serbian")
```

