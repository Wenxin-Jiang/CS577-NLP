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

# deberta-base-chinese

## Model Description

This is a DeBERTa(V2) model pre-trained on Chinese Wikipedia texts (both simplified and traditional). NVIDIA A100-SXM4-40GB took 102 hours 34 minutes for training. You can fine-tune `deberta-base-chinese` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/deberta-base-chinese-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/deberta-base-chinese-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-base-chinese")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/deberta-base-chinese")
```

