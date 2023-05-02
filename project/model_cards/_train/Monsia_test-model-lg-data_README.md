---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: test-model-lg-data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-model-lg-data

This model is a fine-tuned version of [Monsia/test-model-lg-data](https://huggingface.co/Monsia/test-model-lg-data) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3354
- Wer: 0.4150

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0236        | 0.67  | 100  | 0.4048          | 0.4222 |
| 0.0304        | 1.35  | 200  | 0.4266          | 0.4809 |
| 0.0545        | 2.03  | 300  | 0.4309          | 0.4735 |
| 0.0415        | 2.7   | 400  | 0.4269          | 0.4595 |
| 0.033         | 3.38  | 500  | 0.4085          | 0.4537 |
| 0.0328        | 4.05  | 600  | 0.3642          | 0.4224 |
| 0.0414        | 4.73  | 700  | 0.3354          | 0.4150 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.13.3
- Tokenizers 0.10.3
