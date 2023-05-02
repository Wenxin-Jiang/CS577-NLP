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

# deberta-base-japanese-aozora

## Model Description

This is a DeBERTa(V2) model pre-trained on 青空文庫 texts. NVIDIA A100-SXM4-40GB took 36 hours 44 minutes for training. You can fine-tune `deberta-base-japanese-aozora` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-luw-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-aozora-ud-head), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-base-japanese-aozora")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/deberta-base-japanese-aozora")
```

## Reference

安岡孝一: [青空文庫DeBERTaモデルによる国語研長単位係り受け解析](http://hdl.handle.net/2433/275409), 東洋学へのコンピュータ利用, 第35回研究セミナー (2022年7月), pp.29-43.

