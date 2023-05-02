---
license: apache-2.0
language: ar
datasets:
- AymanMansour/SDN-Dialect-Dataset
- arbml/sudanese_dialect_speech
- arabic_speech_corpus
tags:
- generated_from_trainer

metrics:
- wer 
model-index:
- name: openai/whisper-small
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: SDN-Dialect-Dataset
      type: AymanMansour/SDN-Dialect-Dataset
      args: 'config: hi, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 56.3216
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# openai/whisper-small

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5091
- Wer: 56.3216

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
| 0.0157        | 13.0  | 1000 | 1.1631          | 65.9101 |
| 0.0025        | 26.0  | 2000 | 1.3416          | 58.5066 |
| 0.0009        | 39.01 | 3000 | 1.4238          | 56.6398 |
| 0.0004        | 52.01 | 4000 | 1.4800          | 56.3004 |
| 0.0002        | 65.01 | 5000 | 1.5091          | 56.3216 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
