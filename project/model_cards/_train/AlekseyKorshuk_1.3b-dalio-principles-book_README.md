---
license: other
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: 1.3b-dalio-principles-book
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 1.3b-dalio-principles-book

This model is a fine-tuned version of [facebook/opt-1.3b](https://huggingface.co/facebook/opt-1.3b) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4512
- Accuracy: 0.4741

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 8
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.95) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6914        | 0.14  | 1    | 2.6895          | 0.4477   |
| 2.6897        | 0.29  | 2    | 2.6895          | 0.4477   |
| 2.668         | 0.43  | 3    | 2.7031          | 0.4403   |
| 2.7434        | 0.57  | 4    | 2.5918          | 0.4533   |
| 2.6265        | 0.71  | 5    | 2.5410          | 0.4618   |
| 2.5259        | 0.86  | 6    | 2.5156          | 0.4641   |
| 2.5566        | 1.0   | 7    | 2.4902          | 0.4667   |
| 2.2317        | 1.14  | 8    | 2.4766          | 0.4707   |
| 2.2397        | 1.29  | 9    | 2.4727          | 0.4705   |
| 2.0162        | 1.43  | 10   | 2.4766          | 0.4690   |
| 2.0537        | 1.57  | 11   | 2.4805          | 0.4707   |
| 2.1432        | 1.71  | 12   | 2.4707          | 0.4714   |
| 2.0822        | 1.86  | 13   | 2.4570          | 0.4724   |
| 1.9056        | 2.0   | 14   | 2.4512          | 0.4741   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
