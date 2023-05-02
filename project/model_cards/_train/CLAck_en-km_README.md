---
tags:
- translation
---
This model translate from English to Khmer.
It is the pure fine-tuned version of MarianMT model en-zh.
This is the result after 30 epochs of pure fine-tuning of khmer language.

### Example
```
%%capture
!pip install transformers transformers[sentencepiece]

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# Download the pretrained model for English-Vietnamese available on the hub
model = AutoModelForSeq2SeqLM.from_pretrained("CLAck/en-km")

tokenizer = AutoTokenizer.from_pretrained("CLAck/en-km")
# Download a tokenizer that can tokenize English since the model Tokenizer doesn't know anymore how to do it
# We used the one coming from the initial model
# This tokenizer is used to tokenize the input sentence
tokenizer_en = AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-zh')
# These special tokens are needed to reproduce the original tokenizer
tokenizer_en.add_tokens(["<2zh>", "<2khm>"], special_tokens=True)

sentence = "The cat is on the table"
# This token is needed to identify the target language
input_sentence = "<2khm> " + sentence 
translated = model.generate(**tokenizer_en(input_sentence, return_tensors="pt", padding=True))
output_sentence = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
```