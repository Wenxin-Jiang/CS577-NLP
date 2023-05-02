---
license: mit
tags:
- generated_from_trainer
model-index:
- name: gpt2-kit-TLDR
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-kit-TLDR

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6706

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
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 6    | 3.5139          |
| No log        | 2.0   | 12   | 2.8465          |
| No log        | 3.0   | 18   | 2.4698          |
| No log        | 4.0   | 24   | 2.2862          |
| No log        | 5.0   | 30   | 2.1564          |
| No log        | 6.0   | 36   | 2.0529          |
| No log        | 7.0   | 42   | 1.9766          |
| No log        | 8.0   | 48   | 1.9204          |
| No log        | 9.0   | 54   | 1.8798          |
| No log        | 10.0  | 60   | 1.8424          |
| No log        | 11.0  | 66   | 1.8088          |
| No log        | 12.0  | 72   | 1.7897          |
| No log        | 13.0  | 78   | 1.7650          |
| No log        | 14.0  | 84   | 1.7472          |
| No log        | 15.0  | 90   | 1.7345          |
| No log        | 16.0  | 96   | 1.7275          |
| No log        | 17.0  | 102  | 1.7161          |
| No log        | 18.0  | 108  | 1.7056          |
| No log        | 19.0  | 114  | 1.6984          |
| No log        | 20.0  | 120  | 1.6913          |
| No log        | 21.0  | 126  | 1.6857          |
| No log        | 22.0  | 132  | 1.6875          |
| No log        | 23.0  | 138  | 1.6876          |
| No log        | 24.0  | 144  | 1.6846          |
| No log        | 25.0  | 150  | 1.6813          |
| No log        | 26.0  | 156  | 1.6776          |
| No log        | 27.0  | 162  | 1.6740          |
| No log        | 28.0  | 168  | 1.6725          |
| No log        | 29.0  | 174  | 1.6716          |
| No log        | 30.0  | 180  | 1.6706          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Tokenizers 0.12.1
