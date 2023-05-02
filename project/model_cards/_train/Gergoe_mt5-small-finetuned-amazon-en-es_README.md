---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-amazon-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-amazon-en-es

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2891
- Rouge1: 15.35
- Rouge2: 6.4925
- Rougel: 14.8921
- Rougelsum: 14.6312

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 7.0622        | 1.0   | 1276  | 3.5617          | 13.2417 | 4.8928 | 12.8258 | 12.8078   |
| 4.0768        | 2.0   | 2552  | 3.4329          | 14.5681 | 6.4922 | 14.0621 | 13.9709   |
| 3.7736        | 3.0   | 3828  | 3.3393          | 15.1942 | 6.5262 | 14.7138 | 14.6049   |
| 3.5951        | 4.0   | 5104  | 3.3122          | 14.8813 | 6.2962 | 14.507  | 14.3477   |
| 3.477         | 5.0   | 6380  | 3.2991          | 15.0992 | 6.3888 | 14.8397 | 14.5606   |
| 3.4084        | 6.0   | 7656  | 3.3035          | 15.1897 | 6.2292 | 14.6686 | 14.4488   |
| 3.3661        | 7.0   | 8932  | 3.2959          | 15.3489 | 6.5702 | 14.9211 | 14.701    |
| 3.3457        | 8.0   | 10208 | 3.2891          | 15.35   | 6.4925 | 14.8921 | 14.6312   |


### Framework versions

- Transformers 4.19.1
- Pytorch 1.7.0
- Datasets 2.2.1
- Tokenizers 0.12.1
