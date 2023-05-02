---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Multi-ling-BERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Multi-ling-BERT

This model is a fine-tuned version of [bert-base-multilingual-uncased](https://huggingface.co/bert-base-multilingual-uncased) on an unknown dataset.

## Usage

### In Transformers
```python

from transformers import pipeline,AutoTokenizer

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "I feel happy today!"

inputs = tokenizer(text,return_tensors="pt",padding=True, truncation=True)

{
  'input_ids': tensor([[ 101, 1045, 2514, 3407, 2651,  999,  102]]),
   'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1]])
}

tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

['[CLS]', 'i', 'feel', 'happy', 'today', '!', '[SEP]']


tokenizer.decode(inputs["input_ids"][0])
[CLS] i feel happy today! [SEP]



text = "This is the question"
query = "This is the context with lots of information. Some useless. The answer is here some more words."

inputs = tokenizer(text,query,return_tensors="pt",padding=True, truncation=True)

{
  'input_ids': tensor([  101,  2023,  2003,  1996,  3160,   102,  2023,  2003,  1996,  6123,
         2007,  7167,  1997,  2592,  1012,  2070, 11809,  1012,  1996,  3437,
         2003,  2182,  2070,  2062,  2616,  1012,   102])
}

tokenizer.decode(inputs ["input_ids"][0])



text = "I feel happy today!"


# BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained(model_name)
inputs_for_BertTokenizer = tokenizer(text, return_tensors="pt",padding=False, truncation=True, max_length=512, stride=256)

{
  'input_ids': tensor([[  101,   100, 11297,  9200, 11262,   106,   102]]), 
  'token_type_ids': tensor([[0, 0, 0, 0, 0, 0, 0]]), 
  'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1]])
}

# BartTokenizerFast

tokenizer = BartTokenizerFast.from_pretrained("facebook/bart-base")
inputs_for_BartTokenizerFast= tokenizer(text, return_tensors="pt",padding=False, truncation=True, max_length=512, stride=256)

{
  'input_ids': tensor([[   0,  100,  619, 1372,  452,  328,    2]]), 
  'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1]])
}



# Model

from transformers import AutoModel

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModel.from_pretrained(model_name)
outputs = model(**inputs)

print(outputs.last_hidden_state.shape)

{
  torch.Size([1, 7, 768])
}


from transformers import AutoModelForSequenceClassification

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
outputs = model(**inputs)

print(outputs.logits)

{
  tensor([[-4.3450,  4.6878]], grad_fn=<AddmmBackward0>)
}

import torch

predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
print(predictions)

{
  tensor([[1.1942e-04, 9.9988e-01]], grad_fn=<SoftmaxBackward0>)
}


```
