---
language:
- id
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- google/fleurs
- indonesian-nlp/librivox-indonesia
- mozilla-foundation/common_voice_11_0
metrics:
- wer
- cer
model-index:
- name: Whisper Medium ID - FLEURS-CV-LBV - Augmented
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
      value: 7.17
      name: WER
    - type: cer
      value: 2.39
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
      value: 7.59
      name: WER
    - type: cer
      value: 2.33
      name: CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: indonesian-nlp/librivox-indonesia
      type: indonesian-nlp/librivox-indonesia
      config: ind
      split: test
    metrics:
    - type: wer
      value: 6.07
      name: WER
    - type: cer
      value: 1.84
      name: CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium ID - FLEURS-CV-LBV - Augmented

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the following datasets:
- [mozilla-foundation/common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0)
- [google/fleurs](https://huggingface.co/datasets/google/fleurs)
- [indonesian-nlp/librivox-indonesia](https://huggingface.co/datasets/indonesian-nlp/librivox-indonesia)

It achieves the following results on the evaluation set (Common Voice 11.0):
- Loss: 0.2788
- Wer: 7.6132
- Cer: 2.3332

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

Training:
- [mozilla-foundation/common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) (train+validation)
- [google/fleurs](https://huggingface.co/datasets/google/fleurs) (train+validation)
- [indonesian-nlp/librivox-indonesia](https://huggingface.co/datasets/indonesian-nlp/librivox-indonesia) (train)

Evaluation:
- [mozilla-foundation/common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) (test)
- [google/fleurs](https://huggingface.co/datasets/google/fleurs) (test)
- [indonesian-nlp/librivox-indonesia](https://huggingface.co/datasets/indonesian-nlp/librivox-indonesia) (test)

## Training procedure

Datasets were augmented on-the-fly using [audiomentations](https://github.com/iver56/audiomentations) via PitchShift, AddGaussianNoise and TimeStretch transformations at `p=0.3`.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|
| 0.3002        | 1.9   | 1000  | 0.1659          | 8.1850 | 2.5333 |
| 0.0514        | 3.8   | 2000  | 0.1818          | 8.0559 | 2.5244 |
| 0.0145        | 5.7   | 3000  | 0.2150          | 7.8945 | 2.5281 |
| 0.0037        | 7.6   | 4000  | 0.2248          | 7.7100 | 2.3738 |
| 0.0016        | 9.51  | 5000  | 0.2402          | 7.6224 | 2.3591 |
| 0.0009        | 11.41 | 6000  | 0.2525          | 7.7654 | 2.3952 |
| 0.0005        | 13.31 | 7000  | 0.2609          | 7.5994 | 2.3487 |
| 0.0008        | 15.21 | 8000  | 0.2682          | 7.5855 | 2.3347 |
| 0.0002        | 17.11 | 9000  | 0.2756          | 7.6178 | 2.3288 |
| 0.0002        | 19.01 | 10000 | 0.2788          | 7.6132 | 2.3332 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
