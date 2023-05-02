---
language:
- "ja"
tags:
- "japanese"
- "masked-lm"
- "wikipedia"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
widget:
- text: "酸素ボンベを充[MASK]する。"
---

# bert-base-japanese-char-extended

## Model Description

This is a BERT model pre-trained on Japanese Wikipedia texts, derived from [bert-base-japanese-char-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v2). Character-embeddings are enhanced to include all 常用漢字/人名用漢字 characters using BertTokenizerFast. You can fine-tune `bert-base-japanese-char-extended` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/bert-base-japanese-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/bert-base-japanese-wikipedia-ud-head), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/bert-base-japanese-char-extended")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/bert-base-japanese-char-extended")
```

