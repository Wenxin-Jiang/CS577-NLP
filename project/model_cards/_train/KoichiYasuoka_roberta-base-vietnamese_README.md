---
language:
- "vi"
tags:
- "vietnamese"
- "masked-lm"
- "wikipedia"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# roberta-base-vietnamese

## Model Description

This is a RoBERTa model pre-trained on Vietnamese Wikipedia texts. NVIDIA A100-SXM4-40GB took 20 hours 11 minutes for training. You can fine-tune `roberta-base-vietnamese` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-vietnamese-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-base-vietnamese-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-vietnamese")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-vietnamese")
```

