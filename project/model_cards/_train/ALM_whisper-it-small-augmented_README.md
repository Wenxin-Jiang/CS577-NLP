---
language:
- it
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Italian - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 it
      type: mozilla-foundation/common_voice_11_0
      config: it
      split: test
      args: it
    metrics:
    - name: WER
      type: wer
      value: 8.00
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Italian - Robust

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 it dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1980
- Wer: 8.7457

**IMPORTANT** The model has been trained using *data augmentation* to improve its generalization capabilities and robustness. The results on the eval set during training are biased towards data augmentation applied to evaluation data.

**Results on eval set**

- Mozilla CV 11.0 - Italian: 8.00 wer (using official script)
- TODO

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
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 25000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.1927        | 1.0   | 2500  | 0.2506          | 14.9991 |
| 0.0736        | 2.01  | 5000  | 0.2258          | 12.7864 |
| 0.0413        | 3.01  | 7500  | 0.2144          | 11.4508 |
| 0.0201        | 4.02  | 10000 | 0.2146          | 10.8774 |
| 0.0129        | 5.02  | 12500 | 0.2127          | 10.6920 |
| 0.0091        | 6.03  | 15000 | 0.2117          | 10.2867 |
| 0.0043        | 7.03  | 17500 | 0.2076          | 9.6860  |
| 0.0018        | 8.04  | 20000 | 0.2065          | 9.4235  |
| 0.0013        | 9.04  | 22500 | 0.2003          | 8.9105  |
| 0.0009        | 10.05 | 25000 | 0.1978          | 8.7497  |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
