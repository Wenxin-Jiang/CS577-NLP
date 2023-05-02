---
license: mit
tags:
- generated_from_trainer
- token-classification
datasets:
- xtreme
metrics:
- f1
model-index:
- name: xlm-roberta-base-finetuned-arman-fa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-arman-fa

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0077
- F1: 0.9855

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.1054        | 1.0   | 2305  | 0.0497          | 0.8548 |
| 0.0419        | 2.0   | 4610  | 0.0339          | 0.8834 |
| 0.0185        | 3.0   | 6915  | 0.0159          | 0.9626 |
| 0.0068        | 4.0   | 9220  | 0.0103          | 0.9789 |
| 0.0025        | 5.0   | 11525 | 0.0077          | 0.9855 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.9.1
- Datasets 2.1.0
- Tokenizers 0.12.1
