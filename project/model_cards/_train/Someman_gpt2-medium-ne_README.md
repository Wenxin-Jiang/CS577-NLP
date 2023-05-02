---
language: ne
license: mit
tags:
- generated_from_trainer
- gpt2
- ne
datasets: Oscar
widget:
-  text: "गर्मि मौसममा चिसो खाने"
---

# gpt2-medium-ne

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on Oscar Dataset.

## Model description

This model is trained on Oscar Nepali Dataset.

## How to use

You can use this model directly with a pipeline for text generation.

```python
>>> from transformers import pipeline, set_seed
>>> generator = pipeline('text-generation', model='Someman/gpt2-medium-ne')
>>> set_seed(42)
>>> generator("उच्च अदालतले बिहीबार दिएको आदेशले", max_length=30, num_return_sequences=5)

[{'generated_text': 'उच्च अदालतले बिहीबार दिएको आदेशले महिनात्रि'},
 {'generated_text': 'उच्च अदालतले बिहीबार दिएको आदेशले बिहानैदे'},
 {'generated_text': 'उच्च अदालतले बिहीबार दिएको आदेशले गिरिजाली'},
 {'generated_text': 'उच्च अदालतले बिहीबार दिएको आदेशले गरेको प्रथम त'},
 {'generated_text': 'उच्च अदालतले बिहीबार दिएको आदेशले कुनै साथी'}]
```


Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('Someman/gpt2-medium-ne')
model = GPT2Model.from_pretrained('Someman/gpt2-medium-ne')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

and in TensorFlow:

```python
from transformers import GPT2Tokenizer, TFGPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('Someman/gpt2-medium-ne')
model = TFGPT2Model.from_pretrained('Someman/gpt2-medium-ne')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
```


More information needed

## Training and evaluation data

Training data contains 197k Nepali sentences.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 1

### Training results



### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
