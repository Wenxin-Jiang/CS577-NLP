---
language:
- "ain"
tags:
- "ainu"
- "masked-lm"
license: "cc-by-sa-4.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
---

# roberta-base-ainu

## Model Description

This is a RoBERTa model pre-trained on Ainu texts written in カタカナ, Roman, and Кириллица. You can fine-tune `roberta-base-ainu` for downstream tasks, such as [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-base-ainu-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-base-ainu-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-ainu")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-base-ainu")
```

## Reference

安岡孝一: [ローマ字・カタカナ・キリル文字併用アイヌ語RoBERTa・DeBERTaモデルの開発](http://id.nii.ac.jp/1001/00224072/), 情報処理学会研究報告, Vol.2023-CH-131『人文科学とコンピュータ』, No.7 (2023年2月18日), pp.1-7.

