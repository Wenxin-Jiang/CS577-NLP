---
language:
- ru
tags:
- PyTorch
- Transformers

---
# ebanko-base
Model was finetuned by [black_samorez](https://github.com/BlackSamorez).

Based off [sberbank-ai/ruT5-base](https://huggingface.co/sberbank-ai/ruT5-base).

Finetuned on [
russe_detox_2022](https://github.com/skoltech-nlp/russe_detox_2022) train to toxify text.

I recommend using it with **temperature = 1.5**

* Task: `text2text generation`
* Type: `encoder-decoder`
* Tokenizer: `bpe`
* Dict size: `32 101`
* Num Parameters: `222 M`	

---
license: apache-2.0
---
