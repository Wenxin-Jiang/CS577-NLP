---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-300m-ar-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-ar-7

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 61.6652
- Wer: 0.2222

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
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 6306.7719     | 4.71  | 400  | 617.7255        | 1.0    |
| 1222.8073     | 9.41  | 800  | 81.7446         | 0.3820 |
| 326.9842      | 14.12 | 1200 | 67.3986         | 0.2859 |
| 223.859       | 18.82 | 1600 | 60.8896         | 0.2492 |
| 175.5662      | 23.53 | 2000 | 59.2339         | 0.2256 |
| 146.3602      | 28.24 | 2400 | 61.6652         | 0.2222 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0
- Datasets 1.18.4
- Tokenizers 0.11.6
