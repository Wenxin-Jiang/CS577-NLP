---
language:
- pa
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Large Punjabi - Drishti Sharma
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: pa-IN
      split: test
      args: pa-IN
    metrics:
    - name: Wer
      type: wer
      value: 19.71252566735113
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large Punjabi - Drishti Sharma

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2846
- Wer: 19.7125

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0004        | 8.26  | 1000 | 0.2846          | 19.7125 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
