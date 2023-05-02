---
language:
- "lzh"
tags:
- "classical chinese"
- "literary chinese"
- "ancient chinese"
- "masked-lm"
license: "apache-2.0"
pipeline_tag: "fill-mask"
mask_token: "[MASK]"
widget:
- text: "孟子[MASK]梁惠王"
---

# roberta-classical-chinese-large-char

## Model Description

This is a RoBERTa model pre-trained on Classical Chinese texts, derived from [GuwenBERT-large](https://huggingface.co/ethanyt/guwenbert-large). Character-embeddings are enhanced into traditional/simplified characters. You can fine-tune `roberta-classical-chinese-large-char` for downstream tasks, such as [sentence-segmentation](https://huggingface.co/KoichiYasuoka/roberta-classical-chinese-large-sentence-segmentation), [POS-tagging](https://huggingface.co/KoichiYasuoka/roberta-classical-chinese-large-upos), [dependency-parsing](https://huggingface.co/KoichiYasuoka/roberta-classical-chinese-large-ud-goeswith), and so on.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForMaskedLM
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-classical-chinese-large-char")
model=AutoModelForMaskedLM.from_pretrained("KoichiYasuoka/roberta-classical-chinese-large-char")
```

## See Also

[SuPar-Kanbun](https://github.com/KoichiYasuoka/SuPar-Kanbun): Tokenizer POS-tagger and Dependency-parser for Classical Chinese

