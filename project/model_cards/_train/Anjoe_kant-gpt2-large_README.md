---
license: mit
tags:
- generated_from_trainer
model-index:
- name: kant-gpt2-large
  results: []
---

# kant-gpt2-large

This model is a fine-tuned version of [benjamin/gerpt2-large](https://huggingface.co/benjamin/gerpt2-large). It was trained on the "Akademie Ausgabe" of the works of Immanuel Kant. 
It achieves the following results on the evaluation set:
- Loss: 3.4257

## Model description

A large version of gpt2 

## Intended uses & limitations

It could be used for the analysis of knowledge representation in and extraction from large language models

## Training and evaluation data

Akademie Ausgabe Immanuel Kant

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.4094        | 1.0   | 11308 | 3.3838          |
| 3.0445        | 2.0   | 22616 | 3.3107          |
| 2.7161        | 3.0   | 33924 | 3.3409          |
| 2.4793        | 4.0   | 45232 | 3.4257          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
