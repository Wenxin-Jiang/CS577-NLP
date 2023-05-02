---
language:
- sr
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Serbian - Drishti Sharma
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: sr
      split: test
      args: sr
    metrics:
    - name: Wer
      type: wer
      value: 11.614730878186968
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Serbian - Drishti Sharma

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3873
- Wer: 11.6147

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 800
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.1691        | 1.89  | 100  | 0.2398          | 13.5977 |
| 0.0571        | 3.77  | 200  | 0.2419          | 12.7479 |
| 0.0225        | 5.66  | 300  | 0.2869          | 12.2218 |
| 0.0108        | 7.55  | 400  | 0.3085          | 12.2622 |
| 0.0121        | 9.43  | 500  | 0.3478          | 11.6147 |
| 0.0015        | 11.32 | 600  | 0.3702          | 11.5338 |
| 0.0005        | 13.21 | 700  | 0.3839          | 11.6147 |
| 0.0005        | 15.09 | 800  | 0.3873          | 11.6147 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
