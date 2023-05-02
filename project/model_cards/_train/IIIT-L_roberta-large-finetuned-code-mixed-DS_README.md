---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: roberta-large-finetuned-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-code-mixed-DS

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1340
- Accuracy: 0.7203
- Precision: 0.6584
- Recall: 0.6548
- F1: 0.6558

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9729        | 1.0   | 248  | 0.7491          | 0.6922   | 0.6434    | 0.6625 | 0.6358 |
| 0.7474        | 1.99  | 496  | 0.6947          | 0.7183   | 0.6712    | 0.6915 | 0.6760 |
| 0.5938        | 2.99  | 744  | 0.7370          | 0.7123   | 0.6624    | 0.6839 | 0.6642 |
| 0.4264        | 3.98  | 992  | 0.8820          | 0.7123   | 0.6540    | 0.6636 | 0.6492 |
| 0.2806        | 4.98  | 1240 | 1.2022          | 0.7404   | 0.6807    | 0.6694 | 0.6742 |
| 0.2239        | 5.98  | 1488 | 1.3933          | 0.7223   | 0.6593    | 0.6587 | 0.6568 |
| 0.1585        | 6.97  | 1736 | 1.8543          | 0.7304   | 0.6730    | 0.6763 | 0.6737 |
| 0.1302        | 7.97  | 1984 | 2.0783          | 0.7143   | 0.6495    | 0.6520 | 0.6504 |
| 0.1008        | 8.96  | 2232 | 2.3523          | 0.7183   | 0.6588    | 0.6561 | 0.6552 |
| 0.0793        | 9.96  | 2480 | 2.5260          | 0.7163   | 0.6516    | 0.6566 | 0.6538 |
| 0.0498        | 10.96 | 2728 | 2.6074          | 0.7425   | 0.6902    | 0.6817 | 0.6830 |
| 0.0484        | 11.95 | 2976 | 2.6758          | 0.7284   | 0.6687    | 0.6734 | 0.6709 |
| 0.0409        | 12.95 | 3224 | 2.8658          | 0.7425   | 0.6817    | 0.6756 | 0.6781 |
| 0.0239        | 13.94 | 3472 | 2.9484          | 0.7465   | 0.6980    | 0.6818 | 0.6870 |
| 0.025         | 14.94 | 3720 | 3.0827          | 0.7304   | 0.6778    | 0.6577 | 0.6641 |
| 0.0286        | 15.94 | 3968 | 3.0011          | 0.7183   | 0.6509    | 0.6475 | 0.6491 |
| 0.0264        | 16.93 | 4216 | 3.1581          | 0.7264   | 0.6645    | 0.6563 | 0.6595 |
| 0.009         | 17.93 | 4464 | 3.1200          | 0.7223   | 0.6589    | 0.6561 | 0.6569 |
| 0.012         | 18.92 | 4712 | 3.1364          | 0.7203   | 0.6573    | 0.6503 | 0.6525 |
| 0.017         | 19.92 | 4960 | 3.1340          | 0.7203   | 0.6584    | 0.6548 | 0.6558 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
