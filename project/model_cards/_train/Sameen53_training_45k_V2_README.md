---
tags:
- generated_from_trainer
model-index:
- name: training_45k_V2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# training_45k_V2

This model is a fine-tuned version of [Sameen53/training_45k](https://huggingface.co/Sameen53/training_45k) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: inf
- Wer: 0.1673

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.2583        | 1.26  | 1500 | inf             | 0.1660 |
| 0.2522        | 2.51  | 3000 | inf             | 0.1625 |
| 0.2427        | 3.77  | 4500 | inf             | 0.1665 |
| 0.2333        | 5.02  | 6000 | inf             | 0.1629 |
| 0.2692        | 6.28  | 7500 | inf             | 0.1673 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
