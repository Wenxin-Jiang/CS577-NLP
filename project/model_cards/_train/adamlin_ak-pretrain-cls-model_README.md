---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ak-pretrain-cls-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ak-pretrain-cls-model

This model is a fine-tuned version of [hfl/chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0849
- Accuracy: 0.7876

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Accuracy | Validation Loss |
|:-------------:|:-----:|:------:|:--------:|:---------------:|
| 1.3351        | 1.0   | 30469  | 0.7496   | 1.2050          |
| 1.1401        | 2.0   | 60938  | 0.7554   | 1.1823          |
| 1.0411        | 3.0   | 91407  | 0.7609   | 1.1614          |
| 0.9643        | 4.0   | 121876 | 0.7651   | 1.1544          |
| 0.8659        | 5.0   | 152345 | 0.7704   | 1.1291          |
| 0.8099        | 6.0   | 182814 | 0.7746   | 1.1237          |
| 0.7301        | 7.0   | 213283 | 0.7777   | 1.1136          |
| 0.6964        | 8.0   | 243752 | 0.7826   | 1.1106          |
| 0.6616        | 9.0   | 274221 | 0.7853   | 1.0918          |
| 0.6349        | 10.0  | 304690 | 0.7872   | 1.0876          |
| 0.6349        | 20.0  | 304700 | 1.0813   | 0.7874          |
| 0.6427        | 21.0  | 319935 | 1.1011   | 0.7841          |
| 0.6096        | 22.0  | 335170 | 1.1013   | 0.7848          |
| 0.6029        | 23.0  | 350405 | 1.1027   | 0.7859          |
| 0.5762        | 24.0  | 365640 | 1.0980   | 0.7872          |
| 0.5684        | 25.0  | 380875 | 1.1043   | 0.7873          |
| 0.5385        | 26.0  | 396110 | 1.0954   | 0.7884          |
| 0.5114        | 27.0  | 411345 | 1.0975   | 0.7897          |
| 0.499         | 28.0  | 426580 | 1.1016   | 0.7897          |
| 0.526         | 29.0  | 441815 | 1.0954   | 0.7909          |
| 0.5002        | 30.0  | 457050 | 1.0963   | 0.7913          |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0
- Datasets 2.3.1
- Tokenizers 0.11.6
