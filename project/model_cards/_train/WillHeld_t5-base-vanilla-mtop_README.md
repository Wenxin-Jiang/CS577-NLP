---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-base-vanilla-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-vanilla-mtop

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2080
- Exact Match: 0.6394

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
| 1.0516        | 6.65  | 200  | 0.1173          | 0.5875      |
| 0.0541        | 13.33 | 400  | 0.1130          | 0.6331      |
| 0.0468        | 19.98 | 600  | 0.1290          | 0.6036      |
| 0.0241        | 26.65 | 800  | 0.1306          | 0.6273      |
| 0.0125        | 33.33 | 1000 | 0.1425          | 0.6291      |
| 0.0077        | 39.98 | 1200 | 0.1518          | 0.6345      |
| 0.0054        | 46.65 | 1400 | 0.1643          | 0.6362      |
| 0.004         | 53.33 | 1600 | 0.1718          | 0.6362      |
| 0.0033        | 59.98 | 1800 | 0.1803          | 0.6336      |
| 0.0026        | 66.65 | 2000 | 0.1808          | 0.6394      |
| 0.0021        | 73.33 | 2200 | 0.1915          | 0.6371      |
| 0.0017        | 79.98 | 2400 | 0.1919          | 0.6403      |
| 0.0013        | 86.65 | 2600 | 0.2024          | 0.6358      |
| 0.0011        | 93.33 | 2800 | 0.2049          | 0.6353      |
| 0.0008        | 99.98 | 3000 | 0.2080          | 0.6394      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
