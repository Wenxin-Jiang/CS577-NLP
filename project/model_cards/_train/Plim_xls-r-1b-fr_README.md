---
language:
- fr
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
model-index:
- name: ''
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - FR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2464
- Wer: 0.2220

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 5.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 1.0326        | 0.32  | 1000  | 0.3092          | 0.2718 |
| 1.0828        | 0.65  | 2000  | 0.2843          | 0.2606 |
| 1.0771        | 0.97  | 3000  | 0.2774          | 0.2488 |
| 1.0306        | 1.3   | 4000  | 0.2588          | 0.2351 |
| 1.0052        | 1.62  | 5000  | 0.2483          | 0.2284 |
| 0.9865        | 1.94  | 6000  | 0.2464          | 0.2220 |
| 0.978         | 2.27  | 7000  | 0.2514          | 0.2172 |
| 1.7438        | 2.59  | 8000  | 0.7983          | 0.5072 |
| 2.3309        | 2.92  | 9000  | 1.8917          | 0.9416 |
| 2.1834        | 3.24  | 10000 | 1.7496          | 0.9030 |
| 2.3047        | 3.56  | 11000 | 1.5377          | 0.8747 |
| 2.1378        | 3.89  | 12000 | 1.3501          | 0.7923 |
| 1.9812        | 4.21  | 13000 | 1.2662          | 0.7697 |
| 2.6855        | 4.54  | 14000 | 2.4120          | 0.9902 |
| 2.7482        | 4.86  | 15000 | 2.5341          | 0.9874 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
