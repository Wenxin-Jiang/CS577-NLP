---
language:
- "ja"
tags:
- "japanese"
- "masked-lm"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
widget:
- text: "日本に着いたら[MASK]を訪ねなさい。"
---

# deberta-base-japanese-unidic

## Model Description

This is a DeBERTa(V2) model pre-trained on 青空文庫 texts with BertJapaneseTokenizer. You can fine-tune `deberta-base-japanese-unidic` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-unidic-luw-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-unidic-ud-head), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-base-japanese-unidic")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/deberta-base-japanese-unidic")
```

[fugashi](https://pypi.org/project/fugashi) and [unidic-lite](https://pypi.org/project/unidic-lite) are required.

