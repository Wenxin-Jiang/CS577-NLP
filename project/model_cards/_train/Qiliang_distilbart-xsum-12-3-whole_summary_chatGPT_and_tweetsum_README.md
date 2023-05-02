---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: distilbart-xsum-12-3-whole_summary_chatGPT_and_tweetsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-xsum-12-3-whole_summary_chatGPT_and_tweetsum

This model is a fine-tuned version of [sshleifer/distilbart-xsum-12-3](https://huggingface.co/sshleifer/distilbart-xsum-12-3) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7952
- Rouge1: 45.7353
- Rouge2: 29.1566
- Rougel: 45.8429
- Rougelsum: 45.7353
- Gen Len: 16.6

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 397  | 2.8069          | 42.233  | 23.7538 | 39.2701 | 39.2701   | 17.0    |
| 2.8673        | 2.0   | 794  | 2.7736          | 48.2389 | 29.6927 | 43.5004 | 43.5004   | 17.4    |
| 1.8043        | 3.0   | 1191 | 2.7952          | 45.7353 | 29.1566 | 45.8429 | 45.7353   | 16.6    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.12.1
