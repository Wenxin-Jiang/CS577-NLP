---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-0

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8558
- Accuracy: 0.7183

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
| 0.7088        | 1.0   | 13   | 0.6819          | 0.6154   |
| 0.635         | 2.0   | 26   | 0.6318          | 0.7692   |
| 0.547         | 3.0   | 39   | 0.5356          | 0.7692   |
| 0.3497        | 4.0   | 52   | 0.4456          | 0.6923   |
| 0.1979        | 5.0   | 65   | 0.3993          | 0.7692   |
| 0.098         | 6.0   | 78   | 0.3613          | 0.7692   |
| 0.0268        | 7.0   | 91   | 0.3561          | 0.9231   |
| 0.0137        | 8.0   | 104  | 0.3755          | 0.9231   |
| 0.0083        | 9.0   | 117  | 0.4194          | 0.7692   |
| 0.0065        | 10.0  | 130  | 0.4446          | 0.7692   |
| 0.005         | 11.0  | 143  | 0.4527          | 0.7692   |
| 0.0038        | 12.0  | 156  | 0.4645          | 0.7692   |
| 0.0033        | 13.0  | 169  | 0.4735          | 0.7692   |
| 0.0033        | 14.0  | 182  | 0.4874          | 0.7692   |
| 0.0029        | 15.0  | 195  | 0.5041          | 0.7692   |
| 0.0025        | 16.0  | 208  | 0.5148          | 0.7692   |
| 0.0024        | 17.0  | 221  | 0.5228          | 0.7692   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
