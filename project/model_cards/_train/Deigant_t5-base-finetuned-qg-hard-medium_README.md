---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-finetuned-qg-hard-medium
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-qg-hard-medium

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4711
- Rouge1: 44.656
- Rouge2: 24.9885
- Rougel: 40.9697
- Rougelsum: 41.1529

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 1.0   | 135  | 1.5611          | 37.7779 | 19.4817 | 34.3244 | 34.3904   |
| No log        | 2.0   | 270  | 1.4731          | 41.8894 | 21.8733 | 37.6817 | 37.6942   |
| No log        | 3.0   | 405  | 1.4540          | 43.9334 | 24.786  | 40.4115 | 40.3838   |
| 1.7433        | 4.0   | 540  | 1.4363          | 45.9178 | 26.5837 | 41.7405 | 41.8215   |
| 1.7433        | 5.0   | 675  | 1.4388          | 46.23   | 25.1996 | 41.701  | 41.7289   |
| 1.7433        | 6.0   | 810  | 1.4382          | 46.235  | 25.9074 | 42.3053 | 42.4358   |
| 1.7433        | 7.0   | 945  | 1.4447          | 45.9743 | 26.4922 | 42.107  | 42.244    |
| 1.2283        | 8.0   | 1080 | 1.4490          | 44.3634 | 24.1351 | 40.1315 | 40.2471   |
| 1.2283        | 9.0   | 1215 | 1.4501          | 43.2451 | 23.3871 | 39.7387 | 39.9479   |
| 1.2283        | 10.0  | 1350 | 1.4628          | 44.9832 | 25.2642 | 41.1644 | 41.3158   |
| 1.2283        | 11.0  | 1485 | 1.4621          | 45.6738 | 25.344  | 41.6082 | 41.7572   |
| 1.0817        | 12.0  | 1620 | 1.4667          | 44.6365 | 24.9578 | 40.3016 | 40.4266   |
| 1.0817        | 13.0  | 1755 | 1.4678          | 42.7493 | 22.95   | 38.66   | 38.7194   |
| 1.0817        | 14.0  | 1890 | 1.4708          | 45.2846 | 25.0189 | 41.1739 | 41.3332   |
| 0.9889        | 15.0  | 2025 | 1.4711          | 44.656  | 24.9885 | 40.9697 | 41.1529   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
