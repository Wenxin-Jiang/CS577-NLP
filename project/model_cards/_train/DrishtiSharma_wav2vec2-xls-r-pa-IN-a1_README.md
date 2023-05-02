---
language:
- pa-IN
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
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

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - PA-IN dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1508
- Wer: 0.4908

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.5841        | 9.26  | 500  | 3.2514          | 0.9941 |
| 0.3992        | 18.52 | 1000 | 0.8790          | 0.6107 |
| 0.2409        | 27.78 | 1500 | 1.0012          | 0.6366 |
| 0.1447        | 37.04 | 2000 | 1.0167          | 0.6276 |
| 0.1109        | 46.3  | 2500 | 1.0638          | 0.5653 |
| 0.0797        | 55.56 | 3000 | 1.1447          | 0.5715 |
| 0.0636        | 64.81 | 3500 | 1.1503          | 0.5316 |
| 0.0466        | 74.07 | 4000 | 1.2227          | 0.5386 |
| 0.0372        | 83.33 | 4500 | 1.1214          | 0.5225 |
| 0.0239        | 92.59 | 5000 | 1.1375          | 0.4998 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
