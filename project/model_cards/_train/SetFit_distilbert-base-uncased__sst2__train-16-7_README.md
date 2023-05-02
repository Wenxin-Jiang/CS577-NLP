---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-7

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6952
- Accuracy: 0.5025

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
| 0.6949        | 1.0   | 7    | 0.7252          | 0.2857   |
| 0.6678        | 2.0   | 14   | 0.7550          | 0.2857   |
| 0.6299        | 3.0   | 21   | 0.8004          | 0.2857   |
| 0.5596        | 4.0   | 28   | 0.8508          | 0.2857   |
| 0.5667        | 5.0   | 35   | 0.8464          | 0.2857   |
| 0.367         | 6.0   | 42   | 0.8515          | 0.2857   |
| 0.2706        | 7.0   | 49   | 0.9574          | 0.2857   |
| 0.2163        | 8.0   | 56   | 0.9710          | 0.4286   |
| 0.1024        | 9.0   | 63   | 1.1607          | 0.1429   |
| 0.1046        | 10.0  | 70   | 1.3779          | 0.1429   |
| 0.0483        | 11.0  | 77   | 1.4876          | 0.1429   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
