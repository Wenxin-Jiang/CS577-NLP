---
language:
- ca
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
- google/fleurs
- openslr
- collectivat/tv3_parla
- projecte-aina/parlament_parla
metrics:
- wer
model-index:
- name: Whisper Medium Ca
  results: 
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: ca
      split: test
      args: ca
    metrics:
    - name: Wer
      type: wer
      value: 10.0031
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Ca

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Common Voice 11.0, the Fleurs, the SLR69, the tb3_parla and the parlament_parla datasets.
It achieves the following results on the evaluation set:
- eval_loss: 0.1905
- eval_wer: 10.0031
- eval_runtime: 10456.4485
- eval_samples_per_second: 1.563
- eval_steps_per_second: 0.195
- epoch: 0.2
- step: 2000

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- training_steps: 10000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
