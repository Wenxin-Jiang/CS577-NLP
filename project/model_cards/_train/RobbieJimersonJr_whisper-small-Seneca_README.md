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
- name: Whisper Small Seneca
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
      value: 27.49828990734407
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Seneca

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the audiofolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5983
- Wer: 27.4983

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
- training_steps: 7768
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.1151        | 3.01  | 1000 | 0.4013          | 31.8326 |
| 0.0185        | 6.02  | 2000 | 0.4796          | 30.1660 |
| 0.0062        | 9.03  | 3000 | 0.5143          | 30.0417 |
| 0.0022        | 12.04 | 4000 | 0.5469          | 28.6301 |
| 0.0004        | 16.01 | 5000 | 0.5695          | 27.9522 |
| 0.0001        | 19.01 | 6000 | 0.5891          | 27.5294 |
| 0.0002        | 22.02 | 7000 | 0.5983          | 27.4983 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
