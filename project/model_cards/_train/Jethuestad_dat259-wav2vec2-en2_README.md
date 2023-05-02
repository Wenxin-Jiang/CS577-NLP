---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_1_0
model-index:
- name: dat259-wav2vec2-en2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dat259-wav2vec2-en2

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the common_voice_1_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4036
- Wer: 0.5090

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 300
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.4355        | 1.82  | 200  | 3.0307          | 1.0    |
| 2.1744        | 3.64  | 400  | 1.5661          | 0.7449 |
| 0.5535        | 5.45  | 600  | 1.3005          | 0.5914 |
| 0.3248        | 7.27  | 800  | 1.2481          | 0.5690 |
| 0.2297        | 9.09  | 1000 | 1.2810          | 0.5366 |
| 0.18          | 10.91 | 1200 | 1.3481          | 0.5378 |
| 0.1499        | 12.73 | 1400 | 1.3124          | 0.5350 |
| 0.1283        | 14.55 | 1600 | 1.3668          | 0.5161 |
| 0.1089        | 16.36 | 1800 | 1.3833          | 0.5109 |
| 0.0973        | 18.18 | 2000 | 1.3876          | 0.5075 |
| 0.0897        | 20.0  | 2200 | 1.4036          | 0.5090 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1
