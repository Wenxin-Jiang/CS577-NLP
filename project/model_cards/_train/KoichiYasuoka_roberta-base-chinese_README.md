---
language:
- "zh"
tags:
- "chinese"
- "masked-lm"
- "wikipedia"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# roberta-base-chinese

## Model Description

This is a RoBERTa model pre-trained on Chinese Wikipedia texts (both simplified and traditional). NVIDIA A100-SXM4-40GB took 48 hours 56 minutes for training. You can fine-tune `roberta-base-chinese` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-chinese-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-base-chinese-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-chinese")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-chinese")
```

