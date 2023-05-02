---
language:
- el
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Greek - Robust
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 el
      type: mozilla-foundation/common_voice_11_0
      config: el
      split: test
      args: el
    metrics:
    - name: Wer
      type: wer
      value: 24.322065378900444
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Greek - Robust

This model is a fine-tuned version of [whisper-el-medium-augmented](https://huggingface.co/whisper-el-medium-augmented) on the mozilla-foundation/common_voice_11_0 el dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4312
- Wer: 24.3221

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.0905        | 2.35  | 1000  | 0.5419          | 37.8343 |
| 0.0552        | 4.69  | 2000  | 0.5118          | 34.6954 |
| 0.0329        | 7.04  | 3000  | 0.5332          | 32.3180 |
| 0.0219        | 9.39  | 4000  | 0.5185          | 30.1913 |
| 0.0161        | 11.74 | 5000  | 0.4908          | 32.3366 |
| 0.0063        | 14.08 | 6000  | 0.4741          | 28.4733 |
| 0.0015        | 16.43 | 7000  | 0.4400          | 26.3187 |
| 0.001         | 18.78 | 8000  | 0.4428          | 25.5293 |
| 0.0001        | 21.13 | 9000  | 0.4382          | 25.2043 |
| 0.0014        | 23.47 | 10000 | 0.4328          | 24.3221 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.7.1
- Tokenizers 0.12.1
