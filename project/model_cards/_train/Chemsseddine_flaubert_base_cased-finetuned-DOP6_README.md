---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: flaubert_base_cased-finetuned-DOP6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flaubert_base_cased-finetuned-DOP6

This model is a fine-tuned version of [flaubert/flaubert_base_cased](https://huggingface.co/flaubert/flaubert_base_cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4109
- Accuracy: 0.8591

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.9735        | 1.0   | 110  | 0.6360          | 0.7955   |
| 0.6305        | 2.0   | 220  | 0.4801          | 0.8227   |
| 0.4992        | 3.0   | 330  | 0.4163          | 0.8545   |
| 0.4172        | 4.0   | 440  | 0.4109          | 0.8591   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.12.1
