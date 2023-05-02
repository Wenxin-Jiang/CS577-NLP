---
language:
- en-US
license: apache-2.0
tags:
- minds14
- google/xtreme_s
- generated_from_trainer
datasets:
- xtreme_s
metrics:
- f1
- accuracy
model-index:
- name: xtreme_s_xlsr_300m_minds14.en-US_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xtreme_s_xlsr_300m_minds14.en-US_2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the GOOGLE/XTREME_S - MINDS14.EN-US dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5685
- F1: 0.8747
- Accuracy: 0.8759

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
- distributed_type: multi-GPU
- num_devices: 2
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:--------:|
| 2.6195        | 3.95  | 20   | 2.6348          | 0.0172 | 0.0816   |
| 2.5925        | 7.95  | 40   | 2.6119          | 0.0352 | 0.0851   |
| 2.1271        | 11.95 | 60   | 2.3066          | 0.1556 | 0.1986   |
| 1.2618        | 15.95 | 80   | 1.3810          | 0.6877 | 0.7128   |
| 0.5455        | 19.95 | 100  | 1.0403          | 0.6992 | 0.7270   |
| 0.2571        | 23.95 | 120  | 0.8423          | 0.8160 | 0.8121   |
| 0.3478        | 27.95 | 140  | 0.6500          | 0.8516 | 0.8440   |
| 0.0732        | 31.95 | 160  | 0.7066          | 0.8123 | 0.8156   |
| 0.1092        | 35.95 | 180  | 0.5878          | 0.8767 | 0.8759   |
| 0.0271        | 39.95 | 200  | 0.5994          | 0.8578 | 0.8617   |
| 0.4664        | 43.95 | 220  | 0.7830          | 0.8403 | 0.8440   |
| 0.0192        | 47.95 | 240  | 0.5685          | 0.8747 | 0.8759   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
