---
language:
- en
- vi
tags:
- translation
license: apache-2.0
datasets:
- ALT
metrics:
- sacrebleu
---

This is a finetuning of a MarianMT pretrained on Chinese-English. The target language pair is Vietnamese-English.

### Example
```
%%capture
!pip install transformers transformers[sentencepiece]

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# Download the pretrained model for English-Vietnamese available on the hub
model = AutoModelForSeq2SeqLM.from_pretrained("CLAck/vi-en")

tokenizer = AutoTokenizer.from_pretrained("CLAck/vi-en")

sentence = your_vietnamese_sentence
# This token is needed to identify the source language
input_sentence = "<2vi> " + sentence 
translated = model.generate(**tokenizer(input_sentence, return_tensors="pt", padding=True))
output_sentence = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
```

### Training results

| Epoch | Bleu    |
|:-----:|:-------:|
| 1.0   | 21.3180 |
| 2.0   | 26.8012 |
| 3.0   | 29.3578 |
| 4.0   | 31.5178 |
| 5.0   | 32.8740 |
