---
language:
- is
- en
tags:
- translation
license: mit
---

# mBART 25 SentencePiece tokenizer
This tokenizer is used for Mideind's mBART translation models.
It is based on Facebooks mBART-25 SentencePiece model.
A language token from the original model has been replaced with "is_IS".

Usage example (for debugging):
```python
import sys

from transformers.models import mbart

MODEL_DIR = sys.argv[1]
tokenizer: mbart.MBartTokenizerFast = mbart.MBartTokenizerFast.from_pretrained(
    MODEL_DIR, src_lang="en_XX"
)
is_lang_idx = tokenizer.convert_tokens_to_ids("is_IS")
model = mbart.MBartForConditionalGeneration.from_pretrained(MODEL_DIR)
test_sentence = "This is a test."
input_ids = tokenizer(test_sentence, return_tensors="pt")
print(input_ids)
outputs = model.generate(
    **input_ids, decoder_start_token_id=is_lang_idx
)
print(outputs)
print(tokenizer.batch_decode(outputs))
```