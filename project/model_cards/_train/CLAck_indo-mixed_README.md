---
language:
- en
- id
tags:
- translation
license: apache-2.0
datasets:
- ALT
metrics:
- sacrebleu
---

This model is pretrained on Chinese and Indonesian languages, and fine-tuned on Indonesian language.

### Example
```
%%capture
!pip install transformers transformers[sentencepiece]

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# Download the pretrained model for English-Vietnamese available on the hub
model = AutoModelForSeq2SeqLM.from_pretrained("CLAck/indo-mixed")

tokenizer = AutoTokenizer.from_pretrained("CLAck/indo-mixed")
# Download a tokenizer that can tokenize English since the model Tokenizer doesn't know anymore how to do it
# We used the one coming from the initial model
# This tokenizer is used to tokenize the input sentence
tokenizer_en = AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-zh')
# These special tokens are needed to reproduce the original tokenizer
tokenizer_en.add_tokens(["<2zh>", "<2indo>"], special_tokens=True)

sentence = "The cat is on the table"
# This token is needed to identify the target language
input_sentence = "<2indo> " + sentence 
translated = model.generate(**tokenizer_en(input_sentence, return_tensors="pt", padding=True))
output_sentence = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
```

### Training results
MIXED

| Epoch | Bleu    |
|:-----:|:-------:|
| 1.0   | 24.2579 |
| 2.0   | 30.6287 |
| 3.0   | 34.4417 |
| 4.0   | 36.2577 |
| 5.0   | 37.3488 |

FINETUNING

| Epoch | Bleu    |
|:-----:|:-------:|
| 6.0   | 34.1676 |
| 7.0   | 35.2320 |
| 8.0   | 36.7110 |
| 9.0   | 37.3195 |
| 10.0  | 37.9461 |