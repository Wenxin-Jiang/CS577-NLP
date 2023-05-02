---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: trash_mail_cls_2022
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trash_mail_cls_2022

This model is a fine-tuned version of [hfl/chinese-macbert-base](https://huggingface.co/hfl/chinese-macbert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0005
- Accuracy: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0694        | 1.0   | 546  | 0.0088          | 0.9982   |
| 0.0177        | 2.0   | 1092 | 0.0005          | 1.0      |
| 0.0081        | 3.0   | 1638 | 0.0100          | 0.9973   |
| 0.0014        | 4.0   | 2184 | 0.0063          | 0.9982   |
| 0.0001        | 5.0   | 2730 | 0.0079          | 0.9982   |
| 0.0           | 6.0   | 3276 | 0.0076          | 0.9982   |
| 0.0           | 7.0   | 3822 | 0.0068          | 0.9982   |
| 0.0           | 8.0   | 4368 | 0.0066          | 0.9982   |
| 0.0           | 9.0   | 4914 | 0.0029          | 0.9982   |
| 0.0           | 10.0  | 5460 | 0.0029          | 0.9982   |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.12.0
- Datasets 2.3.1
- Tokenizers 0.11.6
