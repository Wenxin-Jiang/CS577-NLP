---
language:
- "ko"
tags:
- "korean"
- "masked-lm"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# roberta-large-korean-hanja

## Model Description

This is a RoBERTa model pre-trained on Korean texts, derived from [klue/roberta-large](https://huggingface.co/klue/roberta-large). Token-embeddings are enhanced to include all 한문 교육용 기초 한자 and 인명용 한자 characters. You can fine-tune `roberta-large-korean-hanja` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-large-korean-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-large-korean-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-large-korean-hanja")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-large-korean-hanja")
```

