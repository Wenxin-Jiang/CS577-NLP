---
language:
- ba
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Bashkir
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 ba
      type: mozilla-foundation/common_voice_11_0
      config: ba
      split: test
      args: ba
    metrics:
    - name: Wer
      type: wer
      value: 15.072300680807968
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Bashkir

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 ba dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2589
- Wer: 15.0723

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 30000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.1637        | 1.01  | 2000  | 0.2555          | 26.4682 |
| 0.1375        | 2.01  | 4000  | 0.2223          | 21.5394 |
| 0.0851        | 3.02  | 6000  | 0.2086          | 19.6725 |
| 0.0573        | 4.02  | 8000  | 0.2178          | 18.4280 |
| 0.036         | 5.03  | 10000 | 0.2312          | 17.8248 |
| 0.0238        | 6.04  | 12000 | 0.2621          | 17.4096 |
| 0.0733        | 7.04  | 14000 | 0.2120          | 16.5656 |
| 0.0111        | 8.05  | 16000 | 0.2682          | 16.2291 |
| 0.0155        | 9.05  | 18000 | 0.2677          | 15.9242 |
| 0.0041        | 10.06 | 20000 | 0.3178          | 15.9534 |
| 0.0023        | 12.01 | 22000 | 0.3218          | 16.0536 |
| 0.0621        | 13.01 | 24000 | 0.2313          | 15.6169 |
| 0.0022        | 14.02 | 26000 | 0.2887          | 15.1083 |
| 0.0199        | 15.02 | 28000 | 0.2553          | 15.1848 |
| 0.0083        | 16.03 | 30000 | 0.2589          | 15.0723 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
