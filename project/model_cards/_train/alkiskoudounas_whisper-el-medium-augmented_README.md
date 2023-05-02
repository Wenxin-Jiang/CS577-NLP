---
language:
- el
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Greek - Robust
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 el
      type: mozilla-foundation/common_voice_11_0
      config: el
      split: test
      args: el
    metrics:
    - name: Wer
      type: wer
      value: 21.684621099554235
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Greek - Robust

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the mozilla-foundation/common_voice_11_0 el dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3168
- Wer: 21.6846

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.3865        | 1.17  | 500  | 0.5842          | 51.4487 |
| 0.2302        | 2.35  | 1000 | 0.4861          | 39.3202 |
| 0.1321        | 3.52  | 1500 | 0.4536          | 37.4257 |
| 0.0916        | 4.69  | 2000 | 0.4103          | 39.6824 |
| 0.0497        | 5.87  | 2500 | 0.4101          | 29.1883 |
| 0.03          | 7.04  | 3000 | 0.4121          | 28.0089 |
| 0.0156        | 8.22  | 3500 | 0.3842          | 26.7459 |
| 0.0037        | 9.39  | 4000 | 0.3433          | 28.7054 |
| 0.0008        | 10.56 | 4500 | 0.3244          | 21.8332 |
| 0.0006        | 11.74 | 5000 | 0.3178          | 21.5267 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.7.1
- Tokenizers 0.12.1
