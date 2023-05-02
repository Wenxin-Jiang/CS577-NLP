---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_10_0
model-index:
- name: fine-tune-Wav2Vec2-XLS-R-300M-Indonesia-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine-tune-Wav2Vec2-XLS-R-300M-Indonesia-test

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice_10_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3076
- Wer: 0.2971

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
- train_batch_size: 7
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 14
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.9436        | 9.99  | 570  | 2.7467          | 1.0    |
| 1.0498        | 19.99 | 1140 | 0.3630          | 0.3965 |
| 0.6789        | 29.99 | 1710 | 0.3396          | 0.3712 |
| 0.5259        | 39.99 | 2280 | 0.3204          | 0.3241 |
| 0.4701        | 49.99 | 2850 | 0.3118          | 0.3005 |
| 0.4248        | 59.99 | 3420 | 0.3076          | 0.2971 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.10.0+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
