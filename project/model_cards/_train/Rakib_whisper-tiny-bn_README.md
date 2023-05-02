---
language:
- bn
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Tiny Bengali
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 bn
      type: mozilla-foundation/common_voice_11_0
      config: bn
      split: test
      args: bn
    metrics:
    - name: Wer
      type: wer
      value: 32.89771261927907
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Tiny Bengali

This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the mozilla-foundation/common_voice_11_0 bn dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2314
- Wer: 32.8977

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.3362        | 0.96  | 1000 | 0.3536          | 45.0860 |
| 0.2395        | 1.91  | 2000 | 0.2745          | 37.1714 |
| 0.205         | 2.87  | 3000 | 0.2485          | 34.7353 |
| 0.1795        | 3.83  | 4000 | 0.2352          | 33.2469 |
| 0.1578        | 4.78  | 5000 | 0.2314          | 32.8977 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
