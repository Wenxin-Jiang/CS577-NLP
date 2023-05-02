---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-4

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5001
- Accuracy: 0.7650

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7175        | 1.0   | 13   | 0.6822          | 0.5385   |
| 0.6559        | 2.0   | 26   | 0.6533          | 0.6154   |
| 0.6052        | 3.0   | 39   | 0.5762          | 0.7692   |
| 0.4587        | 4.0   | 52   | 0.4477          | 0.8462   |
| 0.2459        | 5.0   | 65   | 0.4288          | 0.7692   |
| 0.1001        | 6.0   | 78   | 0.5219          | 0.7692   |
| 0.0308        | 7.0   | 91   | 0.8540          | 0.7692   |
| 0.014         | 8.0   | 104  | 0.7789          | 0.7692   |
| 0.0083        | 9.0   | 117  | 0.7996          | 0.7692   |
| 0.0064        | 10.0  | 130  | 0.8342          | 0.7692   |
| 0.0049        | 11.0  | 143  | 0.8612          | 0.7692   |
| 0.0036        | 12.0  | 156  | 0.8834          | 0.7692   |
| 0.0032        | 13.0  | 169  | 0.9067          | 0.7692   |
| 0.003         | 14.0  | 182  | 0.9332          | 0.7692   |
| 0.0028        | 15.0  | 195  | 0.9511          | 0.7692   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
