---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-base-vanilla-top_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-vanilla-top_v2

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0349

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

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.9322        | 0.82  | 200  | 0.0776          |
| 0.0758        | 1.65  | 400  | 0.0476          |
| 0.0732        | 2.47  | 600  | 0.0762          |
| 0.0527        | 3.29  | 800  | 0.0416          |
| 0.0448        | 4.12  | 1000 | 0.0449          |
| 0.0401        | 4.94  | 1200 | 0.0368          |
| 0.0312        | 5.76  | 1400 | 0.0351          |
| 0.0268        | 6.58  | 1600 | 0.0353          |
| 0.0239        | 7.41  | 1800 | 0.0351          |
| 0.0219        | 8.23  | 2000 | 0.0353          |
| 0.0202        | 9.05  | 2200 | 0.0346          |
| 0.0184        | 9.88  | 2400 | 0.0345          |
| 0.017         | 10.7  | 2600 | 0.0352          |
| 0.0163        | 11.52 | 2800 | 0.0351          |
| 0.0154        | 12.35 | 3000 | 0.0349          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
