---
license: mit
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-booksum-finetuned-booksum-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-booksum-finetuned-booksum-test

This model is a fine-tuned version of [cnicu/t5-small-booksum](https://huggingface.co/cnicu/t5-small-booksum) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2739
- Rouge1: 22.7829
- Rouge2: 4.8349
- Rougel: 18.2465
- Rougelsum: 19.2417

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 3.5123        | 1.0   | 8750  | 3.2816          | 21.7712 | 4.3046 | 17.4053 | 18.4707   |
| 3.2347        | 2.0   | 17500 | 3.2915          | 22.2938 | 4.7828 | 17.8567 | 18.9135   |
| 3.0892        | 3.0   | 26250 | 3.2568          | 22.4966 | 4.825  | 18.0344 | 19.1306   |
| 2.9837        | 4.0   | 35000 | 3.2952          | 22.6913 | 5.0322 | 18.176  | 19.2751   |
| 2.9028        | 5.0   | 43750 | 3.2626          | 22.3548 | 4.7521 | 17.8681 | 18.7815   |
| 2.8441        | 6.0   | 52500 | 3.2691          | 22.6279 | 4.932  | 18.1051 | 19.0763   |
| 2.8006        | 7.0   | 61250 | 3.2753          | 22.8911 | 4.8954 | 18.1204 | 19.1464   |
| 2.7742        | 8.0   | 70000 | 3.2739          | 22.7829 | 4.8349 | 18.2465 | 19.2417   |


### Framework versions

- Transformers 4.19.1
- Pytorch 1.7.0
- Datasets 2.2.1
- Tokenizers 0.12.1
