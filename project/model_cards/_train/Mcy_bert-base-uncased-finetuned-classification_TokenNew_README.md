---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned-classification_TokenNew
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-classification_TokenNew

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 41.4553
- Mse: 41.4553
- Mae: 4.7280
- R2: 0.7658
- Accuracy: 0.1600
- Msev: 0.0241

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Mse     | Mae    | R2     | Accuracy | Msev   |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:------:|:--------:|:------:|
| 10.3178       | 1.0   | 5215  | 41.8852         | 41.8852 | 4.6705 | 0.7634 | 0.1827   | 0.0239 |
| 3.6731        | 2.0   | 10430 | 45.6101         | 45.6101 | 4.9092 | 0.7423 | 0.1809   | 0.0219 |
| 2.0891        | 3.0   | 15645 | 42.1319         | 42.1319 | 4.7640 | 0.7620 | 0.1525   | 0.0237 |
| 1.5213        | 4.0   | 20860 | 42.0646         | 42.0646 | 4.7562 | 0.7623 | 0.1588   | 0.0238 |
| 1.1904        | 5.0   | 26075 | 42.0155         | 42.0155 | 4.7778 | 0.7626 | 0.1563   | 0.0238 |
| 1.0127        | 6.0   | 31290 | 41.6389         | 41.6389 | 4.7342 | 0.7647 | 0.1660   | 0.0240 |
| 0.9218        | 7.0   | 36505 | 40.9860         | 40.9860 | 4.7009 | 0.7684 | 0.1589   | 0.0244 |
| 0.7466        | 8.0   | 41720 | 40.1809         | 40.1809 | 4.6686 | 0.7730 | 0.1629   | 0.0249 |
| 0.7264        | 9.0   | 46935 | 40.9795         | 40.9795 | 4.7043 | 0.7685 | 0.1616   | 0.0244 |
| 0.6968        | 10.0  | 52150 | 41.4553         | 41.4553 | 4.7280 | 0.7658 | 0.1600   | 0.0241 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
