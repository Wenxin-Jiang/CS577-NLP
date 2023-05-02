---
language:
- ur
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small UR 
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      args: 'config: ur, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 41.698656429942424
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small UR - Muhammad Abdullah

This model is a fine-tuned version of [openai/whisper-Small](https://huggingface.co/openai/whisper-large) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9758
- Wer: 41.6987

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 10
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 3500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0074        | 9.62  | 1000 | 0.8238          | 42.0345 |
| 0.0003        | 19.23 | 2000 | 0.9381          | 42.6583 |
| 0.0002        | 28.85 | 3000 | 0.9758          | 41.6987 |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
