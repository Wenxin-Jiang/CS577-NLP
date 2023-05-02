---
language:
- "be"
tags:
- "belarusian"
- "masked-lm"
license: "cc-by-sa-4.0"
datasets:
- "cc100"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# roberta-small-belarusian

## Model Description

This is a RoBERTa model pre-trained on [CC-100](https://data.statmt.org/cc-100/). You can fine-tune `roberta-small-belarusian` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-small-belarusian-upos), dependency-parsing, and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-small-belarusian")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-small-belarusian")
```

