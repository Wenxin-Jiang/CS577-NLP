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

# roberta-base-thai-spm

## Model Description

This is a RoBERTa model pre-trained on Thai Wikipedia texts. You can fine-tune `roberta-base-thai-spm` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-thai-spm-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-base-thai-spm-ud-head), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-thai-spm")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-thai-spm")
```

