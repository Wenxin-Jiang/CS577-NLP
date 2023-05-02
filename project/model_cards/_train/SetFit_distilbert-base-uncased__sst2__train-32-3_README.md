---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5694
- Accuracy: 0.7073

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
| 0.7118        | 1.0   | 13   | 0.6844          | 0.5385   |
| 0.6587        | 2.0   | 26   | 0.6707          | 0.6154   |
| 0.6067        | 3.0   | 39   | 0.6295          | 0.5385   |
| 0.4714        | 4.0   | 52   | 0.5811          | 0.6923   |
| 0.2444        | 5.0   | 65   | 0.5932          | 0.7692   |
| 0.1007        | 6.0   | 78   | 0.7386          | 0.6923   |
| 0.0332        | 7.0   | 91   | 0.6962          | 0.6154   |
| 0.0147        | 8.0   | 104  | 0.8200          | 0.7692   |
| 0.0083        | 9.0   | 117  | 0.9250          | 0.7692   |
| 0.0066        | 10.0  | 130  | 0.9345          | 0.7692   |
| 0.005         | 11.0  | 143  | 0.9313          | 0.7692   |
| 0.0036        | 12.0  | 156  | 0.9356          | 0.7692   |
| 0.0031        | 13.0  | 169  | 0.9395          | 0.7692   |
| 0.0029        | 14.0  | 182  | 0.9504          | 0.7692   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
