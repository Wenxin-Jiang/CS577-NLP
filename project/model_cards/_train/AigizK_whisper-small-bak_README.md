---
license: apache-2.0
tags:
- generated_from_trainer
- whisper-event
datasets:
- common_voice_11_0
metrics:
- wer
model-index:
- name: openai/whisper-small
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: common_voice_11_0
      type: common_voice_11_0
      config: ba
      split: test
      args: ba
    metrics:
    - name: Wer
      type: wer
      value: 20.90095725311917
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# openai/whisper-small

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the common_voice_11_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2116
- Wer: 20.9010

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
| 0.2362        | 0.2   | 1000 | 0.3219          | 35.4541 |
| 0.1566        | 1.04  | 2000 | 0.2583          | 27.1784 |
| 0.1325        | 1.24  | 3000 | 0.2447          | 24.9120 |
| 0.129         | 2.07  | 4000 | 0.2217          | 22.3117 |
| 0.1375        | 2.27  | 5000 | 0.2116          | 20.9010 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
