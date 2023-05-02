---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-small-vanilla-top_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-vanilla-top_v2

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0358
- Exact Match: 0.4268

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 1.8739        | 0.82  | 200  | 0.1319          | 0.2831      |
| 0.1338        | 1.65  | 400  | 0.0670          | 0.3859      |
| 0.0879        | 2.47  | 600  | 0.0568          | 0.4023      |
| 0.0689        | 3.29  | 800  | 0.0478          | 0.4083      |
| 0.059         | 4.12  | 1000 | 0.0457          | 0.4157      |
| 0.0514        | 4.94  | 1200 | 0.0419          | 0.4178      |
| 0.046         | 5.76  | 1400 | 0.0398          | 0.4202      |
| 0.0422        | 6.58  | 1600 | 0.0396          | 0.4220      |
| 0.0386        | 7.41  | 1800 | 0.0386          | 0.4221      |
| 0.0366        | 8.23  | 2000 | 0.0384          | 0.4233      |
| 0.0346        | 9.05  | 2200 | 0.0370          | 0.4249      |
| 0.0322        | 9.88  | 2400 | 0.0362          | 0.4253      |
| 0.0306        | 10.7  | 2600 | 0.0371          | 0.4258      |
| 0.0297        | 11.52 | 2800 | 0.0361          | 0.4266      |
| 0.029         | 12.35 | 3000 | 0.0358          | 0.4268      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
