---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6248
- Accuracy: 0.6826

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
| 0.7136        | 1.0   | 13   | 0.6850          | 0.5385   |
| 0.6496        | 2.0   | 26   | 0.6670          | 0.6154   |
| 0.5895        | 3.0   | 39   | 0.6464          | 0.7692   |
| 0.4271        | 4.0   | 52   | 0.6478          | 0.7692   |
| 0.2182        | 5.0   | 65   | 0.6809          | 0.6923   |
| 0.103         | 6.0   | 78   | 0.9119          | 0.6923   |
| 0.0326        | 7.0   | 91   | 1.0718          | 0.6923   |
| 0.0154        | 8.0   | 104  | 1.0721          | 0.7692   |
| 0.0087        | 9.0   | 117  | 1.1416          | 0.7692   |
| 0.0067        | 10.0  | 130  | 1.2088          | 0.7692   |
| 0.005         | 11.0  | 143  | 1.2656          | 0.7692   |
| 0.0037        | 12.0  | 156  | 1.3104          | 0.7692   |
| 0.0032        | 13.0  | 169  | 1.3428          | 0.6923   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
