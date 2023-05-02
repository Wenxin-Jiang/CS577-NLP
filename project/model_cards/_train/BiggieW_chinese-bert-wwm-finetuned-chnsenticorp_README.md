---
license: apache-2.0
tags:
- generated_from_trainer
widget:
- '积极：这个酒店周围环境真的[MASK]。'
model-index:
- name: chinese-bert-wwm-finetuned-chnsenticorp
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# chinese-bert-wwm-finetuned-chnsenticorp

This model is a fine-tuned version of [hfl/chinese-bert-wwm](https://huggingface.co/hfl/chinese-bert-wwm) on a small subset of chnsenticorp dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0868

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
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.0096        | 1.0   | 15   | 3.7742          |
| 1.7336        | 2.0   | 30   | 3.9102          |
| 2.5286        | 3.0   | 45   | 3.4744          |
| 2.8892        | 4.0   | 60   | 3.1142          |
| 2.7188        | 5.0   | 75   | 2.7622          |
| 2.7923        | 6.0   | 90   | 3.1119          |
| 2.4094        | 7.0   | 105  | 3.0426          |
| 2.5928        | 8.0   | 120  | 2.8928          |
| 2.4072        | 9.0   | 135  | 2.9462          |
| 2.4349        | 10.0  | 150  | 2.7645          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
