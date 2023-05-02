---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- google/fleurs
metrics:
- wer
model-index:
- name: Whisper Medium MS - Augmented
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: ms_my
      split: test
      args: ms_my
    metrics:
    - type: wer
      value: 9.578362255965294
      name: WER
    - type: cer
      value: 2.8109053797929726
      name: CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium MS - Augmented

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the google/fleurs dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2066
- Wer: 9.5784
- Cer: 2.8109

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

Training:
- [google/fleurs](https://huggingface.co/datasets/google/fleurs) (train+validation)

Evaluation:
- [google/fleurs](https://huggingface.co/datasets/google/fleurs) (test)

## Training procedure

Datasets were augmented on-the-fly using [audiomentations](https://github.com/iver56/audiomentations) via PitchShift and TimeStretch transformations at `p=0.3`.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|
| 0.0876        | 2.15  | 200  | 0.1949          | 10.3105 | 3.0685 |
| 0.0064        | 4.3   | 400  | 0.1974          | 9.7004  | 2.9596 |
| 0.0014        | 6.45  | 600  | 0.2031          | 9.6190  | 2.8955 |
| 0.001         | 8.6   | 800  | 0.2058          | 9.6055  | 2.8440 |
| 0.0009        | 10.75 | 1000 | 0.2066          | 9.5784  | 2.8109 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
