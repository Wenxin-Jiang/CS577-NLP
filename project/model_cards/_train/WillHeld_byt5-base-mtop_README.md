---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mtop
model-index:
- name: byt5-base-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# byt5-base-mtop

This model is a fine-tuned version of [google/byt5-base](https://huggingface.co/google/byt5-base) on the mtop dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0704
- Exact Match: 0.7978

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 0.5459        | 6.65  | 200  | 0.0964          | 0.2107      |
| 0.0433        | 13.33 | 400  | 0.0704          | 0.3056      |
| 0.0153        | 19.98 | 600  | 0.0764          | 0.3025      |
| 0.0081        | 26.65 | 800  | 0.0815          | 0.3123      |
| 0.0045        | 33.33 | 1000 | 0.0904          | 0.3065      |
| 0.003         | 39.98 | 1200 | 0.0945          | 0.3060      |
| 0.0021        | 46.65 | 1400 | 0.0969          | 0.3087      |
| 0.0016        | 53.33 | 1600 | 0.1017          | 0.3105      |
| 0.0015        | 59.98 | 1800 | 0.1001          | 0.3096      |
| 0.001         | 66.65 | 2000 | 0.1059          | 0.3087      |
| 0.0006        | 73.33 | 2200 | 0.1041          | 0.3105      |
| 0.0005        | 79.98 | 2400 | 0.1083          | 0.3083      |
| 0.0003        | 86.65 | 2600 | 0.1115          | 0.3096      |
| 0.0002        | 93.33 | 2800 | 0.1130          | 0.3119      |
| 0.0002        | 99.98 | 3000 | 0.1131          | 0.3114      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
