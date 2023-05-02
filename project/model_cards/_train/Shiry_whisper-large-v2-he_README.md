---
language:
- he
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- google/fleurs
metrics:
- wer
model-index:
- name: Whisper Large-V2 Hebrew
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: he_il
      split: train+validation
      args: he_il
    metrics:
    - name: Wer
      type: wer
      value: 27
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large-V2 Hebrew

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the google/fleurs he_il dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5483
- Wer: 27

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- training_steps: 200
- mixed_precision_training: Native AMP


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2