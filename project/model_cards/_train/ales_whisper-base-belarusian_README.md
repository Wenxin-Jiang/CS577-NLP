---
language:
- be
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Base Belarusian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 be
      type: mozilla-foundation/common_voice_11_0
      config: be
      split: validation
      args: be
    metrics:
    - name: Wer
      type: wer
      value: 12.206885082321635
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Base Belarusian

This model is a fine-tuned version of [openai/whisper-base](https://huggingface.co/openai/whisper-base) on the mozilla-foundation/common_voice_11_0 be dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1080
- Wer: 12.2069

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 6000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.2445        | 0.17  | 1000 | 0.3059          | 32.4163 |
| 0.1823        | 0.33  | 2000 | 0.2004          | 22.1259 |
| 0.1412        | 0.5   | 3000 | 0.1752          | 20.0700 |
| 0.1093        | 0.67  | 4000 | 0.1413          | 16.0533 |
| 0.1137        | 0.83  | 5000 | 0.1155          | 13.3108 |
| 0.0585        | 1.1   | 6000 | 0.1080          | 12.2069 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
