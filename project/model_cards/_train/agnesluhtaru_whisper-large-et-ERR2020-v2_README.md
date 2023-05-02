---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-large-et-ERR2020-v2
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: et
      split: test
    metrics:
    - type: wer
      value: 17.4
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-large-et-ERR2020-v2

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2915
- Wer: 13.8640

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
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.2158        | 0.1   | 1000  | 0.3205          | 23.8154 |
| 0.0897        | 0.2   | 2000  | 0.2961          | 18.3340 |
| 0.0785        | 0.3   | 3000  | 0.2839          | 17.5230 |
| 0.0653        | 0.4   | 4000  | 0.2847          | 17.8752 |
| 0.0541        | 0.5   | 5000  | 0.2906          | 15.2645 |
| 0.0566        | 0.6   | 6000  | 0.2845          | 15.2081 |
| 0.051         | 0.7   | 7000  | 0.2888          | 14.4668 |
| 0.049         | 1.03  | 8000  | 0.2927          | 15.3130 |
| 0.044         | 1.13  | 9000  | 0.2915          | 13.8640 |
| 0.0379        | 1.23  | 10000 | 0.2913          | 16.5773 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+rocm5.1.1
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
