---
language:
- lv
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Latvian - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 lv
      type: mozilla-foundation/common_voice_11_0
      config: lv
      split: test
      args: lv
    metrics:
    - type: wer
      value: 33.111954459203034
      name: Wer
    - type: wer
      value: 26.86
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Latvian - Robust

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 lv dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5621
- Wer: 33.1120

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
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0219        | 16.67 | 1000 | 0.6129          | 41.1575 |
| 0.0029        | 33.33 | 2000 | 0.5975          | 36.1480 |
| 0.0003        | 50.0  | 3000 | 0.5626          | 33.6812 |
| 0.0004        | 66.67 | 4000 | 0.5608          | 33.2827 |
| 0.0001        | 83.33 | 5000 | 0.5715          | 33.8046 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
