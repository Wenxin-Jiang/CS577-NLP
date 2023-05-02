---
language:
- pl
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small PL
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: pl
      split: test
      args: pl
    metrics:
    - name: Wer
      type: wer
      value: 8.820627727705968
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium PL

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3739
- Wer: 8.8206

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

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.121         | 0.1   | 500  | 0.2630          | 10.2804 |
| 0.0474        | 1.1   | 1000 | 0.2561          | 9.5597  |
| 0.0257        | 2.09  | 1500 | 0.2617          | 9.5681  |
| 0.0119        | 3.09  | 2000 | 0.2901          | 9.1534  |
| 0.0064        | 4.08  | 2500 | 0.3463          | 9.0280  |
| 0.0045        | 5.08  | 3000 | 0.3151          | 9.0965  |
| 0.0015        | 6.08  | 3500 | 0.3985          | 8.9611  |
| 0.0007        | 7.07  | 4000 | 0.4218          | 8.8073  |
| 0.0006        | 8.07  | 4500 | 0.4054          | 8.8156  |
| 0.0005        | 9.07  | 5000 | 0.3739          | 8.8206  |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
