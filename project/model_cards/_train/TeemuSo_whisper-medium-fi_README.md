---
language:
- fi
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
model-index:
- name: Whisper Medium Fi - Teemu Sormunen
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: fi
      split: test
      args: fi
    metrics:
    - name: Wer
      type: wer
      value: 16.3871
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Fi - Teemu Sormunen

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Common Voice 11.0, train+val dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2453
- eval_wer: 16.3871
- eval_runtime: 1296.4339
- eval_samples_per_second: 1.314
- eval_steps_per_second: 0.164
- epoch: 5.04
- step: 300

## Model description

Checkpoint of a Finnish model trained with Common Voice 11.0 train+validation data. The data is very small, and already during 300 steps the model overfit on training data.


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
- lr_scheduler_warmup_steps: 300
- training_steps: 1000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
