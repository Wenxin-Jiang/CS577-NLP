---
language:
- en
tags:
- grammatical error correction
- text2text
- t5
license: apache-2.0
datasets:
- clang-8
- conll-14
- conll-13
metrics:
- f0.5
---

This model is an implementation of the paper [A Simple Recipe for Multilingual Grammatical Error Correction](https://arxiv.org/pdf/2106.03830.pdf) from Google where they report the State of the art score in the task of Grammatical Error Correction (GEC).
We implement the version with the T5-small with the reported F_0.5 score in the paper (60.70).

To effectively use the "Hosted inference API", write "gec: [YOUR SENTENCE HERE]".

In order to use the model, look at the following snippet:
```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained("Unbabel/gec-t5_small")
tokenizer = T5Tokenizer.from_pretrained('t5-small')

sentence = "I like to swimming"
tokenized_sentence = tokenizer('gec: ' + sentence, max_length=128, truncation=True, padding='max_length', return_tensors='pt')
corrected_sentence = tokenizer.decode(
    model.generate(
        input_ids = tokenized_sentence.input_ids,
        attention_mask = tokenized_sentence.attention_mask, 
        max_length=128,
        num_beams=5,
        early_stopping=True,
    )[0],
    skip_special_tokens=True, 
    clean_up_tokenization_spaces=True
)
print(corrected_sentence) # -> I like swimming.
```