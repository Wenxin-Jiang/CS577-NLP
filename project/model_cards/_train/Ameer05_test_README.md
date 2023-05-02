---
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test

This model is a fine-tuned version of [Ameer05/tokenizer-repo](https://huggingface.co/Ameer05/tokenizer-repo) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6109
- Rouge1: 54.9442
- Rouge2: 45.3299
- Rougel: 50.5219
- Rougelsum: 53.6475

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 0.91  | 5    | 2.3705          | 53.62   | 44.3835 | 49.6135 | 52.693    |
| No log        | 1.91  | 10   | 1.9035          | 47.478  | 37.0934 | 39.7935 | 45.1881   |
| No log        | 2.91  | 15   | 1.7990          | 54.2488 | 45.0782 | 49.8421 | 52.7564   |
| No log        | 3.91  | 20   | 1.7125          | 55.7903 | 46.7554 | 52.2733 | 54.9389   |
| 2.4456        | 4.91  | 25   | 1.6421          | 52.2279 | 43.4391 | 49.6955 | 51.2915   |
| 2.4456        | 5.91  | 30   | 1.6102          | 55.8598 | 47.3293 | 53.1337 | 54.8596   |
| 2.4456        | 6.91  | 35   | 1.6164          | 53.7902 | 44.6622 | 49.5045 | 52.2304   |
| 2.4456        | 7.91  | 40   | 1.6015          | 51.5597 | 42.0333 | 47.9639 | 50.1154   |
| 1.239         | 8.91  | 45   | 1.6067          | 53.0301 | 43.7214 | 49.0227 | 51.8109   |
| 1.239         | 9.91  | 50   | 1.6109          | 54.9442 | 45.3299 | 50.5219 | 53.6475   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.1
- Datasets 2.0.0
- Tokenizers 0.10.3
