---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bart-base-finetuned-mbti-0830
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-finetuned-mbti-0830

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.0023        | 1.0   | 9920  | 0.0000          |
| 0.0005        | 2.0   | 19840 | 0.0000          |
| 0.0002        | 3.0   | 29760 | 0.0000          |
| 0.0001        | 4.0   | 39680 | 0.0000          |
| 0.0001        | 5.0   | 49600 | 0.0000          |
| 0.0           | 6.0   | 59520 | 0.0000          |
| 0.0           | 7.0   | 69440 | 0.0000          |
| 0.0           | 8.0   | 79360 | 0.0000          |
| 0.0           | 9.0   | 89280 | 0.0000          |
| 0.0           | 10.0  | 99200 | 0.0000          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
