---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-base-checkpoint-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-checkpoint-5

This model is a fine-tuned version of [jiobiala24/wav2vec2-base-checkpoint-4](https://huggingface.co/jiobiala24/wav2vec2-base-checkpoint-4) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9849
- Wer: 0.3354

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.3947        | 1.96  | 1000  | 0.5749          | 0.3597 |
| 0.2856        | 3.93  | 2000  | 0.6212          | 0.3479 |
| 0.221         | 5.89  | 3000  | 0.6280          | 0.3502 |
| 0.1755        | 7.86  | 4000  | 0.6517          | 0.3526 |
| 0.1452        | 9.82  | 5000  | 0.7115          | 0.3481 |
| 0.1256        | 11.79 | 6000  | 0.7687          | 0.3509 |
| 0.1117        | 13.75 | 7000  | 0.7785          | 0.3490 |
| 0.0983        | 15.72 | 8000  | 0.8115          | 0.3442 |
| 0.0877        | 17.68 | 9000  | 0.8290          | 0.3429 |
| 0.0799        | 19.65 | 10000 | 0.8517          | 0.3412 |
| 0.0733        | 21.61 | 11000 | 0.9370          | 0.3448 |
| 0.066         | 23.58 | 12000 | 0.9157          | 0.3410 |
| 0.0623        | 25.54 | 13000 | 0.9673          | 0.3377 |
| 0.0583        | 27.5  | 14000 | 0.9804          | 0.3348 |
| 0.0544        | 29.47 | 15000 | 0.9849          | 0.3354 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
