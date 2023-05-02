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
- name: Whisper Small Chinese Base
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: google/fleurs cmn_hans_cn
      type: google/fleurs
      config: cmn_hans_cn
      split: test
      args: cmn_hans_cn
    metrics:
    - name: Wer
      type: wer
      value: 16.643891773708663
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Chinese Base

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the google/fleurs cmn_hans_cn dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3573
- Wer: 16.6439

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
| 0.0005        | 76.0  | 1000 | 0.3573          | 16.6439 |
| 0.0002        | 153.0 | 2000 | 0.3897          | 16.9749 |
| 0.0001        | 230.0 | 3000 | 0.4125          | 17.2330 |
| 0.0001        | 307.0 | 4000 | 0.4256          | 17.2451 |
| 0.0001        | 384.0 | 5000 | 0.4330          | 17.2300 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
