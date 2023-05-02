---
license: apache-2.0
tags:
- summarisation
- generated_from_trainer
metrics:
- rouge
model-index:
- name: distilbart-xsum-6-6-finetuned-bbc-news-on-abstractive
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-xsum-6-6-finetuned-bbc-news-on-abstractive

This model is a fine-tuned version of [sshleifer/distilbart-xsum-6-6](https://huggingface.co/sshleifer/distilbart-xsum-6-6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6549
- Rouge1: 38.9186
- Rouge2: 30.2223
- Rougel: 32.6201
- Rougelsum: 37.7502

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
| 1.3838        | 1.0   | 445  | 1.4841          | 39.1621 | 30.4379 | 32.6613 | 37.9963   |
| 1.0077        | 2.0   | 890  | 1.5173          | 39.388  | 30.9125 | 33.099  | 38.2442   |
| 0.7983        | 3.0   | 1335 | 1.5726          | 38.7913 | 30.0766 | 32.6092 | 37.5953   |
| 0.6681        | 4.0   | 1780 | 1.6549          | 38.9186 | 30.2223 | 32.6201 | 37.7502   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
