---
language:
- "th"
tags:
- "thai"
- "masked-lm"
- "wikipedia"
license: "apache-2.0"
pipeline_tag: "fill-mask"
mask_token: "<mask>"
widget:
- text: "แผนกนี้กำลัง<mask>กับความท้าทายใหม่"
---

# roberta-base-thai-syllable

## Model Description

This is a RoBERTa model pre-trained on Thai Wikipedia texts, derived from [wangchanberta-base-wiki-syllable](https://huggingface.co/airesearch/wangchanberta-base-wiki-syllable). Character-embeddings are modified to use BertTokenizerFast. You can fine-tune `roberta-base-thai-syllable` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-thai-syllable-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-base-thai-syllable-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-thai-syllable")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-thai-syllable")
```

