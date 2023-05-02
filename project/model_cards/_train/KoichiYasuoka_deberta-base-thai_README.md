---
language:
- "th"
tags:
- "thai"
- "masked-lm"
- "wikipedia"
license: "apache-2.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# deberta-base-thai

## Model Description

This is a DeBERTa(V2) model pre-trained on Thai Wikipedia texts. NVIDIA A100-SXM4-40GB took 10 hours 17 minutes for training. You can fine-tune `deberta-base-thai` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/deberta-base-thai-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/deberta-base-thai-ud-head), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-base-thai")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/deberta-base-thai")
```

