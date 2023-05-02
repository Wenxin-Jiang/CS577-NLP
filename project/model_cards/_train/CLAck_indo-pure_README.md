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
Pure fine-tuning version of MarianMT en-zh on Indonesian Language

### Example
```
%%capture
!pip install transformers transformers[sentencepiece]

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# Download the pretrained model for English-Vietnamese available on the hub
model = AutoModelForSeq2SeqLM.from_pretrained("CLAck/indo-pure")

tokenizer = AutoTokenizer.from_pretrained("CLAck/indo-pure")
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

| Epoch | Bleu    |
|:-----:|:-------:|
| 1.0   | 15.9336 |
| 2.0   | 28.0175 |
| 3.0   | 31.6603 |
| 4.0   | 33.9151 |
| 5.0   | 35.0472 |
| 6.0   | 35.8469 |
| 7.0   | 36.1180 |
| 8.0   | 36.6018 |
| 9.0   | 37.1973 |
| 10.0  | 37.2738 |