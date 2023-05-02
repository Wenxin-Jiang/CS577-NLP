---
language:
- ru
tags:
- PyTorch
- Transformers
thumbnail: "https://github.com/sberbank-ai/model-zoo"

---
# ebanko-base
Model was finetuned by [black_samorez](https://github.com/BlackSamorez).

Based off [sberbank-ai/ruT5-base](https://huggingface.co/sberbank-ai/ruT5-base).

Finetuned on [Russian Language Toxic Comments](https://www.kaggle.com/datasets/blackmoon/russian-language-toxic-comments) and [
russe_detox_2022](https://github.com/skoltech-nlp/russe_detox_2022) train to toxify text.
* Task: `text2text generation`
* Type: `encoder-decoder`
* Tokenizer: `bpe`
* Dict size: `32 101 `
* Num Parameters: `737 M`

---
license: apache-2.0
---
