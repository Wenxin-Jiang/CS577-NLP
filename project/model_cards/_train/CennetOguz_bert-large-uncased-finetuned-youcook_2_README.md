---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-large-uncased-finetuned-youcook_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased-finetuned-youcook_2

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9929

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
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.3915        | 1.0   | 206  | 2.1036          |
| 2.0412        | 2.0   | 412  | 2.2207          |
| 1.9062        | 3.0   | 618  | 1.7281          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0a0+17540c5
- Datasets 2.3.2
- Tokenizers 0.12.1
