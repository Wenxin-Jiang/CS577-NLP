---
license: apache-2.0
tags:
- summarisation
- generated_from_trainer
metrics:
- rouge
model-index:
- name: distilbart-xsum-6-6-finetuned-bbc-news
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-xsum-6-6-finetuned-bbc-news

This model is a fine-tuned version of [sshleifer/distilbart-xsum-6-6](https://huggingface.co/sshleifer/distilbart-xsum-6-6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2624
- Rouge1: 62.1927
- Rouge2: 54.4754
- Rougel: 55.868
- Rougelsum: 60.9345

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 0.4213        | 1.0   | 445  | 0.2005          | 59.4886 | 51.7791 | 53.5126 | 58.3405   |
| 0.1355        | 2.0   | 890  | 0.1887          | 61.7474 | 54.2823 | 55.7324 | 60.5787   |
| 0.0891        | 3.0   | 1335 | 0.1932          | 61.1312 | 53.103  | 54.6992 | 59.8923   |
| 0.0571        | 4.0   | 1780 | 0.2141          | 60.8797 | 52.6195 | 54.4402 | 59.5298   |
| 0.0375        | 5.0   | 2225 | 0.2318          | 61.7875 | 53.8753 | 55.5068 | 60.5448   |
| 0.0251        | 6.0   | 2670 | 0.2484          | 62.3535 | 54.6029 | 56.2804 | 61.031    |
| 0.0175        | 7.0   | 3115 | 0.2542          | 61.6351 | 53.8248 | 55.6399 | 60.3765   |
| 0.0133        | 8.0   | 3560 | 0.2624          | 62.1927 | 54.4754 | 55.868  | 60.9345   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
