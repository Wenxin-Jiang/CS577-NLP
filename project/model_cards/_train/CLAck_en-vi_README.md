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

This is a finetuning of a MarianMT pretrained on English-Chinese. The target language pair is English-Vietnamese.
The first phase of training (mixed) is performed on a dataset containing both English-Chinese and English-Vietnamese sentences.
The second phase of training (pure) is performed on a dataset containing only English-Vietnamese sentences.

### Example
```
%%capture
!pip install transformers transformers[sentencepiece]

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# Download the pretrained model for English-Vietnamese available on the hub
model = AutoModelForSeq2SeqLM.from_pretrained("CLAck/en-vi")

tokenizer = AutoTokenizer.from_pretrained("CLAck/en-vi")
# Download a tokenizer that can tokenize English since the model Tokenizer doesn't know anymore how to do it
# We used the one coming from the initial model
# This tokenizer is used to tokenize the input sentence
tokenizer_en = AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-zh')
# These special tokens are needed to reproduce the original tokenizer
tokenizer_en.add_tokens(["<2zh>", "<2vi>"], special_tokens=True)

sentence = "The cat is on the table"
# This token is needed to identify the target language
input_sentence = "<2vi> " + sentence 
translated = model.generate(**tokenizer_en(input_sentence, return_tensors="pt", padding=True))
output_sentence = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
```

### Training results

MIXED

| Epoch | Bleu    |
|:-----:|:-------:|
| 1.0   | 26.2407 |
| 2.0   | 32.6016 |
| 3.0   | 35.4060 |
| 4.0   | 36.6737 |
| 5.0   | 37.3774 |


PURE

| Epoch | Bleu    |
|:-----:|:-------:|
| 1.0   | 37.3169 |
| 2.0   | 37.4407 |
| 3.0   | 37.6696 |
| 4.0   | 37.8765 |
| 5.0   | 38.0105 |

