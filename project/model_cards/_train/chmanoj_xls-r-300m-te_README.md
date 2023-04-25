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
- name: xls-r-300m-te
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
      value: 24.695121951219512
      name: Test WER
    - type: cer
      value: 4.861934182322532
      name: Test CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the OPENSLR_SLR66 - NA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2680
- Wer: 0.3467

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.0304        | 4.81  | 500   | 1.5676          | 1.0554 |
| 1.5263        | 9.61  | 1000  | 0.4693          | 0.8023 |
| 1.5299        | 14.42 | 1500  | 0.4368          | 0.7311 |
| 1.5063        | 19.23 | 2000  | 0.4360          | 0.7302 |
| 1.455         | 24.04 | 2500  | 0.4213          | 0.6692 |
| 1.4755        | 28.84 | 3000  | 0.4329          | 0.5943 |
| 1.352         | 33.65 | 3500  | 0.4074          | 0.5765 |
| 1.3122        | 38.46 | 4000  | 0.3866          | 0.5630 |
| 1.2799        | 43.27 | 4500  | 0.3860          | 0.5480 |
| 1.212         | 48.08 | 5000  | 0.3590          | 0.5317 |
| 1.1645        | 52.88 | 5500  | 0.3283          | 0.4757 |
| 1.0854        | 57.69 | 6000  | 0.3162          | 0.4687 |
| 1.0292        | 62.5  | 6500  | 0.3126          | 0.4416 |
| 0.9607        | 67.31 | 7000  | 0.2990          | 0.4066 |
| 0.9156        | 72.12 | 7500  | 0.2870          | 0.4009 |
| 0.8329        | 76.92 | 8000  | 0.2791          | 0.3909 |
| 0.7979        | 81.73 | 8500  | 0.2770          | 0.3670 |
| 0.7144        | 86.54 | 9000  | 0.2841          | 0.3661 |
| 0.6997        | 91.35 | 9500  | 0.2721          | 0.3485 |
| 0.6568        | 96.15 | 10000 | 0.2681          | 0.3437 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0
