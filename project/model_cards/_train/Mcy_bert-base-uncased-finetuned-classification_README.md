---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-classification

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 38.9115
- Mse: 38.9115
- Mae: 4.5330
- R2: 0.7802
- Accuracy: 0.1620
- Msev: 0.0257

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
| 12.4524       | 1.0   | 5215  | 43.9797         | 43.9797 | 4.8194 | 0.7515 | 0.1693   | 0.0227 |
| 4.393         | 2.0   | 10430 | 39.2333         | 39.2333 | 4.6028 | 0.7783 | 0.1737   | 0.0255 |
| 2.424         | 3.0   | 15645 | 41.3763         | 41.3763 | 4.6597 | 0.7662 | 0.1620   | 0.0242 |
| 1.781         | 4.0   | 20860 | 39.4309         | 39.4309 | 4.5960 | 0.7772 | 0.1767   | 0.0254 |
| 1.3608        | 5.0   | 26075 | 38.9115         | 38.9115 | 4.5330 | 0.7802 | 0.1620   | 0.0257 |
| 1.2014        | 6.0   | 31290 | 39.7403         | 39.7403 | 4.5850 | 0.7755 | 0.1716   | 0.0252 |
| 1.0742        | 7.0   | 36505 | 40.4495         | 40.4495 | 4.6133 | 0.7715 | 0.1685   | 0.0247 |
| 0.837         | 8.0   | 41720 | 39.5864         | 39.5864 | 4.5630 | 0.7763 | 0.1620   | 0.0253 |
| 0.8054        | 9.0   | 46935 | 39.9482         | 39.9482 | 4.5839 | 0.7743 | 0.1569   | 0.0250 |
| 0.8085        | 10.0  | 52150 | 39.5685         | 39.5685 | 4.5669 | 0.7764 | 0.1573   | 0.0253 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
