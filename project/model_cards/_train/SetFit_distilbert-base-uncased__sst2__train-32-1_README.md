---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6492
- Accuracy: 0.6551

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
| 0.7106        | 1.0   | 13   | 0.6850          | 0.6154   |
| 0.631         | 2.0   | 26   | 0.6632          | 0.6923   |
| 0.5643        | 3.0   | 39   | 0.6247          | 0.7692   |
| 0.3992        | 4.0   | 52   | 0.5948          | 0.7692   |
| 0.1928        | 5.0   | 65   | 0.5803          | 0.7692   |
| 0.0821        | 6.0   | 78   | 0.6404          | 0.6923   |
| 0.0294        | 7.0   | 91   | 0.7387          | 0.6923   |
| 0.0141        | 8.0   | 104  | 0.8270          | 0.6923   |
| 0.0082        | 9.0   | 117  | 0.8496          | 0.6923   |
| 0.0064        | 10.0  | 130  | 0.8679          | 0.6923   |
| 0.005         | 11.0  | 143  | 0.8914          | 0.6923   |
| 0.0036        | 12.0  | 156  | 0.9278          | 0.6923   |
| 0.0031        | 13.0  | 169  | 0.9552          | 0.6923   |
| 0.0029        | 14.0  | 182  | 0.9745          | 0.6923   |
| 0.0028        | 15.0  | 195  | 0.9785          | 0.6923   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
