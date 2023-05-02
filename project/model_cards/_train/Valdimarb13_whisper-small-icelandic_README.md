---
language:
- is
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- language-and-voice-lab/samromur_asr
metrics:
- wer
model-index:
- name: Whisper Small Icelandic
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: samromur
      type: language-and-voice-lab/samromur_asr
      config: samromur_asr
      split: test
      args: 'split: test'
    metrics:
    - name: Wer
      type: wer
      value: 23.040907733651835
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Icelandic

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the samromur dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2613
- Wer: 23.0409

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
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.3551        | 0.18  | 1000 | 0.4322          | 35.0421 |
| 0.2541        | 0.36  | 2000 | 0.3249          | 27.4721 |
| 0.231         | 0.53  | 3000 | 0.2781          | 24.2234 |
| 0.2277        | 0.71  | 4000 | 0.2613          | 23.0409 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
