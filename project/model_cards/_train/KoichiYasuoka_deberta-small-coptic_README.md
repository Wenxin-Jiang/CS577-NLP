---
language:
- "cop"
tags:
- "coptic"
- "masked-lm"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# deberta-small-coptic

## Model Description

This is a DeBERTa(V2) model pre-trained on Coptic Scriptorium Corpora. You can fine-tune `deberta-small-coptic` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/deberta-small-coptic-upos), dependency-parsing, and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-small-coptic")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/deberta-small-coptic")
```

