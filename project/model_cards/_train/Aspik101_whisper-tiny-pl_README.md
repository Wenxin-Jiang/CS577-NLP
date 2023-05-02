---
language:
- pl
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Tiny Pl
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: pl
      split: test
      args: pl
    metrics:
    - name: Wer
      type: wer
      value: 39.469591826496995
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Tiny Pl

This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6919
- Wer: 39.4696

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
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.3647        | 1.05  | 500  | 0.6999          | 43.0430 |
| 0.2752        | 3.04  | 1000 | 0.6002          | 39.3275 |
| 0.2513        | 5.04  | 1500 | 0.5911          | 37.8643 |
| 0.1661        | 7.04  | 2000 | 0.6381          | 37.6887 |
| 0.154         | 9.03  | 2500 | 0.6157          | 37.9362 |
| 0.1126        | 11.03 | 3000 | 0.6319          | 38.6402 |
| 0.0763        | 13.02 | 3500 | 0.6539          | 38.9730 |
| 0.0729        | 15.02 | 4000 | 0.6583          | 38.9362 |
| 0.0778        | 17.02 | 4500 | 0.6653          | 39.6769 |
| 0.0698        | 19.01 | 5000 | 0.6919          | 39.4696 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
