---
language:
- "uk"
tags:
- "ukrainian"
- "masked-lm"
- "ubertext"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# roberta-base-ukrainian

## Model Description

This is a RoBERTa model pre-trained on [Корпус UberText](https://lang.org.ua/uk/corpora/#anchor4). You can fine-tune `roberta-base-ukrainian` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-ukrainian-upos), dependency-parsing, and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-ukrainian")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-ukrainian")
```

