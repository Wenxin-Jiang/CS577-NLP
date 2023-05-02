---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-uncased-base
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-uncased-base

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an Reddit-dialogue dataset.
This model can be used for Text Classification: Given two sentences, see if they are related.
It achieves the following results on the evaluation set:
- Loss: 0.2297
- Accuracy: 0.9267

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 320
- eval_batch_size: 80
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.0
- Tokenizers 0.11.0

## Usage (HuggingFace Transformers)
You can use the model like this: 

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# label_list
label_list = ['matched', 'unmatched']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained("Fan-s/reddit-tc-bert", use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained("Fan-s/reddit-tc-bert") 

# Set the input
post = "don't make gravy with asbestos."
response = "i'd expect someone with a culinary background to know that. since we're talking about school dinner ladies, they need to learn this pronto."

# Predict whether the two sentences are matched 
def predict(post, response, max_seq_length=128):
    with torch.no_grad():
        args =  (post, response)
        input = tokenizer(*args, padding="max_length", max_length=max_seq_length, truncation=True, return_tensors="pt")
        output = model(**input)
        logits = output.logits
        item = torch.argmax(logits, dim=1)
        predict_label = label_list[item]
        return predict_label, logits
         
predict_label, logits = predict(post, response)
# Matched
print("predict_label:", predict_label)
```