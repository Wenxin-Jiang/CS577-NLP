---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4805
- Accuracy: 0.7699

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
| 0.7124        | 1.0   | 13   | 0.6882          | 0.5385   |
| 0.6502        | 2.0   | 26   | 0.6715          | 0.5385   |
| 0.6001        | 3.0   | 39   | 0.6342          | 0.6154   |
| 0.455         | 4.0   | 52   | 0.5713          | 0.7692   |
| 0.2605        | 5.0   | 65   | 0.5562          | 0.7692   |
| 0.1258        | 6.0   | 78   | 0.6799          | 0.7692   |
| 0.0444        | 7.0   | 91   | 0.8096          | 0.7692   |
| 0.0175        | 8.0   | 104  | 0.9281          | 0.6923   |
| 0.0106        | 9.0   | 117  | 0.9826          | 0.6923   |
| 0.0077        | 10.0  | 130  | 1.0254          | 0.7692   |
| 0.0056        | 11.0  | 143  | 1.0667          | 0.7692   |
| 0.0042        | 12.0  | 156  | 1.1003          | 0.7692   |
| 0.0036        | 13.0  | 169  | 1.1299          | 0.7692   |
| 0.0034        | 14.0  | 182  | 1.1623          | 0.6923   |
| 0.003         | 15.0  | 195  | 1.1938          | 0.6923   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
