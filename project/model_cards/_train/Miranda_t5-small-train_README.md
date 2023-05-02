---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-train
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-train

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2367
- Rouge1: 43.9525
- Rouge2: 22.3403
- Rougel: 38.7683
- Rougelsum: 39.2056

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.6e-05
- train_batch_size: 9
- eval_batch_size: 9
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 3.3237        | 1.0   | 40   | 2.6713          | 34.4731 | 14.9731 | 29.4814 | 29.9747   |
| 2.7401        | 2.0   | 80   | 2.4318          | 38.1153 | 18.3492 | 33.4476 | 33.9181   |
| 2.5882        | 3.0   | 120  | 2.3339          | 41.2707 | 19.8571 | 36.2685 | 36.6119   |
| 2.4264        | 4.0   | 160  | 2.2878          | 42.184  | 20.9666 | 37.3488 | 37.6172   |
| 2.3915        | 5.0   | 200  | 2.2605          | 43.4928 | 21.7195 | 38.4917 | 38.8471   |
| 2.3599        | 6.0   | 240  | 2.2462          | 44.2876 | 22.28   | 38.9234 | 39.3673   |
| 2.3073        | 7.0   | 280  | 2.2398          | 43.9822 | 22.3746 | 38.7625 | 39.0964   |
| 2.3026        | 8.0   | 320  | 2.2367          | 43.9525 | 22.3403 | 38.7683 | 39.2056   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
