---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-small-vanilla-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-vanilla-mtop

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1581
- Exact Match: 0.6331

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
| 1.5981        | 6.65  | 200  | 0.1598          | 0.4940      |
| 0.1335        | 13.33 | 400  | 0.1155          | 0.5884      |
| 0.074         | 19.98 | 600  | 0.1046          | 0.6094      |
| 0.0497        | 26.65 | 800  | 0.1065          | 0.6139      |
| 0.0363        | 33.33 | 1000 | 0.1134          | 0.6255      |
| 0.0278        | 39.98 | 1200 | 0.1177          | 0.6313      |
| 0.022         | 46.65 | 1400 | 0.1264          | 0.6255      |
| 0.0183        | 53.33 | 1600 | 0.1260          | 0.6304      |
| 0.0151        | 59.98 | 1800 | 0.1312          | 0.6300      |
| 0.0124        | 66.65 | 2000 | 0.1421          | 0.6277      |
| 0.0111        | 73.33 | 2200 | 0.1405          | 0.6277      |
| 0.0092        | 79.98 | 2400 | 0.1466          | 0.6331      |
| 0.008         | 86.65 | 2600 | 0.1522          | 0.6340      |
| 0.007         | 93.33 | 2800 | 0.1590          | 0.6295      |
| 0.0064        | 99.98 | 3000 | 0.1581          | 0.6331      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
