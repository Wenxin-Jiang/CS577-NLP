---
license: apache-2.0
tags:
- summarisation
- generated_from_trainer
metrics:
- rouge
model-index:
- name: distilbart-xsum-6-6-finetuned-bbc-news-on-extractive
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-xsum-6-6-finetuned-bbc-news-on-extractive

This model is a fine-tuned version of [sshleifer/distilbart-xsum-6-6](https://huggingface.co/sshleifer/distilbart-xsum-6-6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5869
- Rouge1: 39.4885
- Rouge2: 31.7487
- Rougel: 31.9013
- Rougelsum: 34.0825

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 1.4649        | 1.0   | 445  | 1.5047          | 39.1053 | 31.6651 | 32.3242 | 33.9332   |
| 1.2224        | 2.0   | 890  | 1.4986          | 39.4115 | 31.7894 | 32.1057 | 34.0454   |
| 1.0099        | 3.0   | 1335 | 1.5322          | 39.5936 | 31.9984 | 32.2283 | 34.1798   |
| 0.8687        | 4.0   | 1780 | 1.5869          | 39.4885 | 31.7487 | 31.9013 | 34.0825   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
