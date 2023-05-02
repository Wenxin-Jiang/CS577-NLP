---
language:
- ab
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

This model is a fine-tuned version of [hf-test/xls-r-dummy](https://huggingface.co/hf-test/xls-r-dummy) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - AB dataset.
It achieves the following results on the evaluation set:
- Loss: 156.8789
- Wer: 1.3456

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 10
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.1.dev0
- Tokenizers 0.11.0