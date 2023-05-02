---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mtop
model-index:
- name: byt5-small-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# byt5-small-mtop

This model is a fine-tuned version of [google/byt5-small](https://huggingface.co/google/byt5-small) on the mtop dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0697
- Exact Match: 0.7620

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 0.5431        | 6.65  | 200  | 0.1532          | 0.0940      |
| 0.073         | 13.33 | 400  | 0.0697          | 0.2823      |
| 0.0247        | 19.98 | 600  | 0.0721          | 0.3007      |
| 0.0128        | 26.65 | 800  | 0.0863          | 0.3038      |
| 0.0082        | 33.33 | 1000 | 0.0950          | 0.3078      |
| 0.0051        | 39.98 | 1200 | 0.0994          | 0.3029      |
| 0.0036        | 46.65 | 1400 | 0.1046          | 0.3074      |
| 0.0027        | 53.33 | 1600 | 0.1022          | 0.3087      |
| 0.0022        | 59.98 | 1800 | 0.1067          | 0.3096      |
| 0.0016        | 66.65 | 2000 | 0.1081          | 0.3101      |
| 0.0011        | 73.33 | 2200 | 0.1141          | 0.3105      |
| 0.0008        | 79.98 | 2400 | 0.1170          | 0.3074      |
| 0.0007        | 86.65 | 2600 | 0.1198          | 0.3083      |
| 0.0006        | 93.33 | 2800 | 0.1212          | 0.3083      |
| 0.0005        | 99.98 | 3000 | 0.1218          | 0.3087      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
