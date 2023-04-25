---
language:
- te
license: apache-2.0
tags:
- automatic-speech-recognition
- openslr_SLR66
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- openslr
- SLR66
metrics:
- wer
model-index:
- name: xls-r-1B-te
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: openslr
      name: Open SLR
      args: SLR66
    metrics:
    - type: wer
      value: 0.51
      name: Test WER
    - type: cer
      value: 0.097
      name: Test CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-2b](https://huggingface.co/facebook/wav2vec2-xls-r-2b) on the OPENSLR_SLR66 - NA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4253
- Wer: 0.5109


### Evaluation metrics

| Metric | Split  | Decode with LM | Value     |
|:------:|:------:|:--------------:|:---------:|
| WER    | Train  | No             |      |
| CER    | Train  | No             |      |
| WER    | Test   | No             |      |
| CER    | Test   | No             |      |
| WER    | Train  | Yes            |      |
| CER    | Train  | Yes            |      |
| WER    | Test   | Yes            |      |
| CER    | Test   | Yes            |      |


## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 12
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- learning_rate: 3e-6
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 150.0
- hidden_dropout: 0.15
- mixed_precision_training: Native AMP

### Training results




### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0
