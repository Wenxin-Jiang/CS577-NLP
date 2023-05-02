---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- NbAiLab/NCC_S
metrics:
- wer
model-index:
- name: Whisper Base Norwegian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NbAiLab/NCC_S
      type: NbAiLab/NCC_S
      config: 'no'
      split: validation
      args: 'no'
    metrics:
    - name: Wer
      type: wer
      value: 15.012180267965894
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Base Norwegian

This model is a fine-tuned version of [pere/whisper-small-nob-clr](https://huggingface.co/pere/whisper-small-nob-clr) on the NbAiLab/NCC_S dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3284
- Wer: 15.0122

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant_with_warmup
- training_steps: 3000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.5975        | 0.33  | 1000 | 0.3354          | 15.7734 |
| 0.5783        | 0.67  | 2000 | 0.3327          | 16.3520 |
| 0.5788        | 1.0   | 3000 | 0.3284          | 15.0122 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
