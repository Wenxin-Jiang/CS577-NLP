---
language:
- vi
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
- google/fleurs
- vivos
metrics:
- wer
model-index:
- name: Whisper Medium VI - Multi - Augmented
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: vi
      split: test
    metrics:
    - type: wer
      value: 16.63
      name: WER
    - type: cer
      value: 7.74
      name: CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: vi_vn
      split: test
    metrics:
    - type: wer
      value: 9.04
      name: WER
    - type: cer
      value: 4.81
      name: CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: vivos
      type: vivos
      split: test
    metrics:
    - type: wer
      value: 8.53
      name: WER
    - type: cer
      value: 3.67
      name: CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium VI - Multi - Augmented

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the following datasets:
- [mozilla-foundation/common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0)
- [google/fleurs](https://huggingface.co/datasets/google/fleurs)
- [vivos](https://huggingface.co/datasets/vivos)

It achieves the following results on the evaluation set:
- Loss: 0.3696
- Wer: 16.6594
- Cer: 7.7625

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

Training:
- [mozilla-foundation/common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) (train+validation)
- [google/fleurs](https://huggingface.co/datasets/google/fleurs) (train+validation)
- [vivos](https://huggingface.co/datasets/vivos) (train)

Evaluation:
- [mozilla-foundation/common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) (test)
- [google/fleurs](https://huggingface.co/datasets/google/fleurs) (test)
- [vivos](https://huggingface.co/datasets/vivos) (test)

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

| Training Loss | Epoch | Step | Validation Loss | Wer     | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|
| 0.1992        | 1.8   | 1000 | 0.2726          | 17.4929 | 8.2562 |
| 0.0402        | 3.6   | 2000 | 0.3317          | 17.4929 | 8.2588 |
| 0.0073        | 5.4   | 3000 | 0.3429          | 17.6793 | 8.8913 |
| 0.0014        | 7.19  | 4000 | 0.3599          | 19.0283 | 9.5103 |
| 0.0006        | 8.99  | 5000 | 0.3696          | 16.6594 | 7.7625 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
