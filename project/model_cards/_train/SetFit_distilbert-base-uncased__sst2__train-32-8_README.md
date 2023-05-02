---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-8

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6880
- Accuracy: 0.5014

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
| 0.712         | 1.0   | 13   | 0.6936          | 0.5385   |
| 0.665         | 2.0   | 26   | 0.6960          | 0.3846   |
| 0.6112        | 3.0   | 39   | 0.7138          | 0.3846   |
| 0.4521        | 4.0   | 52   | 0.8243          | 0.4615   |
| 0.2627        | 5.0   | 65   | 0.7723          | 0.6154   |
| 0.0928        | 6.0   | 78   | 1.2666          | 0.5385   |
| 0.0312        | 7.0   | 91   | 1.2306          | 0.6154   |
| 0.0132        | 8.0   | 104  | 1.3385          | 0.6154   |
| 0.0082        | 9.0   | 117  | 1.4584          | 0.6154   |
| 0.0063        | 10.0  | 130  | 1.5429          | 0.6154   |
| 0.0049        | 11.0  | 143  | 1.5913          | 0.6154   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
