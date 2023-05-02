---
language:
- ms
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- google/fleurs
model-index:
- name: Whisper Medium MS - FLEURS
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: ms_my
      split: test
    metrics:
    - type: wer
      value: 11.75
      name: WER
    - type: cer
      value: 3.49
      name: CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium MS - FLEURS

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the FLEURS dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2941
- eval_wer: 10.2
- eval_runtime: 954.9
- eval_samples_per_second: 0.784
- eval_steps_per_second: 0.049
- epoch: 53.2
- step: 5000

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
- gradient_accumulation_steps: 1
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
