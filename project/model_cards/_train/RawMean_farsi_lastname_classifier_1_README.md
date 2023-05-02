---
license: mit
tags:
- generated_from_trainer
model-index:
- name: farsi_lastname_classifier_1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# farsi_lastname_classifier_1

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0482
- Pearson: 0.9232

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8e-05
- train_batch_size: 128
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| No log        | 1.0   | 12   | 0.2705          | 0.7018  |
| No log        | 2.0   | 24   | 0.0993          | 0.7986  |
| No log        | 3.0   | 36   | 0.0804          | 0.8347  |
| No log        | 4.0   | 48   | 0.0433          | 0.9246  |
| No log        | 5.0   | 60   | 0.0559          | 0.9176  |
| No log        | 6.0   | 72   | 0.0465          | 0.9334  |
| No log        | 7.0   | 84   | 0.0503          | 0.9154  |
| No log        | 8.0   | 96   | 0.0438          | 0.9222  |
| No log        | 9.0   | 108  | 0.0468          | 0.9260  |
| No log        | 10.0  | 120  | 0.0482          | 0.9232  |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
