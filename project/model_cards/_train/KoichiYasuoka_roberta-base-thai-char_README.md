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

# roberta-base-thai-char

## Model Description

This is a RoBERTa model pre-trained on Thai Wikipedia texts with character-wise embeddings to use BertTokenizerFast. You can fine-tune `roberta-base-thai-char` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-thai-char-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-base-thai-char-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-thai-char")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-thai-char")
```

