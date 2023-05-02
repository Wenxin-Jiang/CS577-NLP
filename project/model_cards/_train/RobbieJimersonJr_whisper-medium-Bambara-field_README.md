---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- audiofolder
metrics:
- wer
model-index:
- name: Whisper Medium Bambara Fieldwork
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: audiofolder
      type: audiofolder
      config: default
      split: train
      args: default
    metrics:
    - name: Wer
      type: wer
      value: 157.60036917397323
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Bambara Fieldwork

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the audiofolder dataset.
It achieves the following results on the evaluation set:
- Loss: 4.0725
- Wer: 157.6004

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
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 13532
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer      |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.6342        | 1.03  | 1000  | 2.5810          | 159.5293 |
| 0.2873        | 3.03  | 2000  | 2.9513          | 159.1140 |
| 0.1461        | 5.02  | 3000  | 3.6833          | 158.3941 |
| 0.049         | 7.02  | 4000  | 4.0725          | 157.6004 |
| 0.0218        | 9.01  | 5000  | 4.2531          | 158.3664 |
| 0.0071        | 11.0  | 6000  | 4.5944          | 157.9972 |
| 0.0057        | 12.04 | 7000  | 4.6659          | 161.4952 |
| 0.0061        | 14.03 | 8000  | 4.9162          | 161.0614 |
| 0.0042        | 16.03 | 9000  | 5.0205          | 158.9848 |
| 0.0007        | 18.02 | 10000 | 5.1463          | 159.1970 |
| 0.0015        | 20.01 | 11000 | 5.2150          | 159.0401 |
| 0.0001        | 22.01 | 12000 | 5.3008          | 159.5478 |
| 0.0001        | 24.0  | 13000 | 5.3800          | 159.0309 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
