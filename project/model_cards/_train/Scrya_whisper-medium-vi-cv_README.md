---
language:
- vi
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium VI - CV - Augmented
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: vi
      split: test
      args: vi
    metrics:
    - type: wer
      value: 18.030269796007897
      name: Wer
    - type: wer
      value: 17.98
      name: WER
    - type: cer
      value: 8.31
      name: CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium VI - CV - Augmented

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6613
- Wer: 18.0303
- Cer: 8.3095

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|
| 0.0053        | 11.49 | 1000 | 0.5429          | 18.1290 | 8.4643 |
| 0.0021        | 22.99 | 2000 | 0.5916          | 18.8857 | 8.6538 |
| 0.0001        | 34.48 | 3000 | 0.6348          | 18.3374 | 8.4296 |
| 0.0001        | 45.98 | 4000 | 0.6508          | 17.9754 | 8.3149 |
| 0.0001        | 57.47 | 5000 | 0.6613          | 18.0303 | 8.3095 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
