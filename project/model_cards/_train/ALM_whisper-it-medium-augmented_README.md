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
- name: Whisper Medium Italian - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 it
      type: mozilla-foundation/common_voice_11_0
      config: it
      split: train
      args: it
    metrics:
    - type: wer
      value: 7.651366149266425
      name: Wer
    - type: wer
      value: 6.6
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Italian - Robust

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the mozilla-foundation/common_voice_11_0 it dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1388
- WER (Augmented Test): 7.65

**IMPORTANT** The model has been trained using *data augmentation* to improve its generalization capabilities and robustness. 
The results on the eval set during training are biased towards data augmentation applied to evaluation data.

**Results on eval set**

- Mozilla CV 11.0 - Italian: 6.60 WER (using official script)

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
- training_steps: 7500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.226         | 0.33  | 2500 | 0.2779          | 14.6642 |
| 0.1278        | 1.03  | 5000 | 0.1818          | 10.2049 |
| 0.0304        | 1.36  | 7500 | 0.1388          | 7.5544  |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
