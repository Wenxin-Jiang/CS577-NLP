---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: XLS-R_timit_en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XLS-R_timit_en

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3799
- Wer: 0.3019

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.5228        | 3.3   | 1000 | 0.9889          | 0.8394 |
| 0.6617        | 6.6   | 2000 | 0.3566          | 0.4027 |
| 0.3177        | 9.9   | 3000 | 0.3112          | 0.3606 |
| 0.2262        | 13.2  | 4000 | 0.3521          | 0.3324 |
| 0.1683        | 16.5  | 5000 | 0.3563          | 0.3260 |
| 0.137         | 19.8  | 6000 | 0.3605          | 0.3149 |
| 0.1139        | 23.1  | 7000 | 0.3768          | 0.3069 |
| 0.1068        | 26.4  | 8000 | 0.3643          | 0.3044 |
| 0.0897        | 29.7  | 9000 | 0.3799          | 0.3019 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.0
