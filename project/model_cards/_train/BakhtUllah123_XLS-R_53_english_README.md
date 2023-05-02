---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: XLS-R_53_english
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XLS-R_53_english

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3430
- Wer: 0.3033

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
| 4.6589        | 1.65  | 500  | 3.1548          | 1.0    |
| 2.5363        | 3.3   | 1000 | 1.0250          | 0.8707 |
| 0.849         | 4.95  | 1500 | 0.3964          | 0.4636 |
| 0.4812        | 6.6   | 2000 | 0.3341          | 0.3907 |
| 0.3471        | 8.25  | 2500 | 0.3351          | 0.3659 |
| 0.2797        | 9.9   | 3000 | 0.3104          | 0.3475 |
| 0.2336        | 11.55 | 3500 | 0.3545          | 0.3419 |
| 0.2116        | 13.2  | 4000 | 0.3577          | 0.3353 |
| 0.1688        | 14.85 | 4500 | 0.3383          | 0.3302 |
| 0.1587        | 16.5  | 5000 | 0.3431          | 0.3235 |
| 0.1358        | 18.15 | 5500 | 0.3504          | 0.3209 |
| 0.1323        | 19.8  | 6000 | 0.3468          | 0.3191 |
| 0.115         | 21.45 | 6500 | 0.3331          | 0.3127 |
| 0.108         | 23.1  | 7000 | 0.3497          | 0.3099 |
| 0.0938        | 24.75 | 7500 | 0.3532          | 0.3091 |
| 0.0974        | 26.4  | 8000 | 0.3461          | 0.3086 |
| 0.0867        | 28.05 | 8500 | 0.3422          | 0.3054 |
| 0.0852        | 29.7  | 9000 | 0.3430          | 0.3033 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
