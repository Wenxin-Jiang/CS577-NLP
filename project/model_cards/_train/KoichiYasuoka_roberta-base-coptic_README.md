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

# roberta-base-coptic

## Model Description

This is a RoBERTa model pre-trained on Coptic Scriptorium Corpora. You can fine-tune `roberta-base-coptic` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-coptic-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-base-coptic-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-coptic")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-coptic")
```

