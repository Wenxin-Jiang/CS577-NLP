---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-finetuned-qg-context-dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-qg-context-dataset

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6222
- Rouge1: 36.2283
- Rouge2: 16.0636
- Rougel: 32.6282
- Rougelsum: 32.6551

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 1.0   | 73   | 1.8864          | 32.9447 | 13.9495 | 27.5473 | 27.4092   |
| No log        | 2.0   | 146  | 1.6866          | 35.1131 | 13.7925 | 30.7017 | 30.5957   |
| No log        | 3.0   | 219  | 1.6392          | 30.4209 | 11.2611 | 27.0456 | 27.0847   |
| No log        | 4.0   | 292  | 1.6222          | 36.2283 | 16.0636 | 32.6282 | 32.6551   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
