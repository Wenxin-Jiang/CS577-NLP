---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: AIDman-wav2vec2-large-xls-r-300m-Irish-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AIDman-wav2vec2-large-xls-r-300m-Irish-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2158
- Wer: 0.5657

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
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.1213        | 12.49 | 400  | 1.1994          | 0.7152 |
| 0.3656        | 24.98 | 800  | 1.2158          | 0.5657 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
