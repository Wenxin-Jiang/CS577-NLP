---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: thesis-audio-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# thesis-audio-1

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4268
- Wer: 0.3395

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.4633        | 4.0   | 500  | 1.4892          | 1.0006 |
| 0.5377        | 8.0   | 1000 | 0.4046          | 0.4163 |
| 0.1818        | 12.0  | 1500 | 0.4255          | 0.3850 |
| 0.1024        | 16.0  | 2000 | 0.4574          | 0.3644 |
| 0.0723        | 20.0  | 2500 | 0.4412          | 0.3550 |
| 0.0542        | 24.0  | 3000 | 0.4095          | 0.3404 |
| 0.0434        | 28.0  | 3500 | 0.4268          | 0.3395 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
