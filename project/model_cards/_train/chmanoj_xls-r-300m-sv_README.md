---
language:
- sv-SE
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: ''
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - SV-SE dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8004
- Wer: 0.7139

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.6683        | 1.45  | 500  | 1.7698          | 1.0041 |
| 1.9548        | 2.91  | 1000 | 1.0890          | 0.8602 |
| 1.9568        | 4.36  | 1500 | 1.0878          | 0.8680 |
| 1.9497        | 5.81  | 2000 | 1.1501          | 0.8838 |
| 1.8453        | 7.27  | 2500 | 1.0452          | 0.8418 |
| 1.6952        | 8.72  | 3000 | 0.9153          | 0.7823 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu113
- Datasets 1.18.1.dev0
- Tokenizers 0.10.3
