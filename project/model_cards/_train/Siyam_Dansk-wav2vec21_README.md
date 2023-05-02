---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: Dansk-wav2vec21
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Dansk-wav2vec21

This model is a fine-tuned version of [Siyam/SKYLy](https://huggingface.co/Siyam/SKYLy) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8025
- Wer: 0.4057

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
- lr_scheduler_warmup_steps: 500
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0563        | 4.26  | 400  | 0.7887          | 0.4560 |
| 0.0756        | 8.51  | 800  | 0.7519          | 0.4444 |
| 0.0497        | 12.77 | 1200 | 0.7979          | 0.4256 |
| 0.0335        | 17.02 | 1600 | 0.8025          | 0.4057 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 2.1.0
- Tokenizers 0.10.3
