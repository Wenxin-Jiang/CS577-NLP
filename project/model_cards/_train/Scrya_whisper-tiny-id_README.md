---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
metrics:
- wer
model-index:
- name: Whisper Tiny ID - FLEURS-CV
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: id_id
      split: test
    metrics:
    - type: wer
      value: 30.8
      name: WER
    - type: cer
      value: 11.29
      name: CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: id
      split: test
    metrics:
    - type: wer
      value: 32.49
      name: WER
    - type: cer
      value: 12.25
      name: CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Tiny ID - FLEURS-CV

This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5129
- Wer: 31.1298

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
- train_batch_size: 32
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
| 0.617         | 1.43  | 500  | 0.5956          | 40.1521 |
| 0.4062        | 2.86  | 1000 | 0.4991          | 33.2066 |
| 0.2467        | 4.29  | 1500 | 0.4755          | 31.6802 |
| 0.1904        | 5.71  | 2000 | 0.4681          | 30.5907 |
| 0.118         | 7.14  | 2500 | 0.4776          | 30.9368 |
| 0.0941        | 8.57  | 3000 | 0.4831          | 30.7297 |
| 0.0771        | 10.0  | 3500 | 0.4912          | 31.1014 |
| 0.0536        | 11.43 | 4000 | 0.5043          | 31.2319 |
| 0.0502        | 12.86 | 4500 | 0.5113          | 31.2404 |
| 0.0418        | 14.29 | 5000 | 0.5129          | 31.1298 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
