---
language:
- te
license: apache-2.0
tags:
- automatic-speech-recognition
- openslr_SLR66
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- openslr
- SLR66
metrics:
- wer
model-index:
- name: xls-r-1B-te
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: openslr
      name: Open SLR
      args: SLR66
    metrics:
    - type: wer
      value: 20.624
      name: Test WER
    - type: cer
      value: 3.979
      name: Test CER
    - type: wer
      value: 26.14777618364419
      name: Test WER (without LM)
    - type: cer
      value: 4.932543184970369
      name: Test CER (without LM)
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the OPENSLR_SLR66 - NA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3119
- Wer: 0.2613


### Evaluation metrics

| Metric | Split  | Decode with LM | Value     |
|:------:|:------:|:--------------:|:---------:|
| WER    | Train  | No             | 5.36      |
| CER    | Train  | No             | 1.11      |
| WER    | Test   | No             | 26.14     |
| CER    | Test   | No             | 4.93      |
| WER    | Train  | Yes            | 5.04      |
| CER    | Train  | Yes            | 1.07      |
| WER    | Test   | Yes            | 20.69     |
| CER    | Test   | Yes            | 3.986     |


## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 150.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|
| 2.9038        | 4.8    | 500   | 3.0125          | 1.0    |
| 1.3777        | 9.61   | 1000  | 0.8681          | 0.8753 |
| 1.1436        | 14.42  | 1500  | 0.6256          | 0.7961 |
| 1.0997        | 19.23  | 2000  | 0.5244          | 0.6875 |
| 1.0363        | 24.04  | 2500  | 0.4585          | 0.6276 |
| 0.7996        | 28.84  | 3000  | 0.4072          | 0.5295 |
| 0.825         | 33.65  | 3500  | 0.3590          | 0.5222 |
| 0.8018        | 38.46  | 4000  | 0.3678          | 0.4671 |
| 0.7545        | 43.27  | 4500  | 0.3474          | 0.3962 |
| 0.7375        | 48.08  | 5000  | 0.3224          | 0.3869 |
| 0.6198        | 52.88  | 5500  | 0.3233          | 0.3630 |
| 0.6608        | 57.69  | 6000  | 0.3029          | 0.3308 |
| 0.645         | 62.5   | 6500  | 0.3195          | 0.3722 |
| 0.5249        | 67.31  | 7000  | 0.3004          | 0.3202 |
| 0.4875        | 72.11  | 7500  | 0.2826          | 0.2992 |
| 0.5171        | 76.92  | 8000  | 0.2962          | 0.2976 |
| 0.4974        | 81.73  | 8500  | 0.2990          | 0.2933 |
| 0.4387        | 86.54  | 9000  | 0.2834          | 0.2755 |
| 0.4511        | 91.34  | 9500  | 0.2886          | 0.2787 |
| 0.4112        | 96.15  | 10000 | 0.3093          | 0.2976 |
| 0.4064        | 100.96 | 10500 | 0.3123          | 0.2863 |
| 0.4047        | 105.77 | 11000 | 0.2968          | 0.2719 |
| 0.3519        | 110.57 | 11500 | 0.3106          | 0.2832 |
| 0.3719        | 115.38 | 12000 | 0.3030          | 0.2737 |
| 0.3669        | 120.19 | 12500 | 0.2964          | 0.2714 |
| 0.3386        | 125.0  | 13000 | 0.3101          | 0.2714 |
| 0.3137        | 129.8  | 13500 | 0.3063          | 0.2710 |
| 0.3008        | 134.61 | 14000 | 0.3082          | 0.2617 |
| 0.301         | 139.42 | 14500 | 0.3121          | 0.2628 |
| 0.3291        | 144.23 | 15000 | 0.3105          | 0.2612 |
| 0.3133        | 149.04 | 15500 | 0.3114          | 0.2624 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0
