---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-7

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6953
- Accuracy: 0.5063

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
| 0.6911        | 1.0   | 7    | 0.7455          | 0.2857   |
| 0.6844        | 2.0   | 14   | 0.7242          | 0.2857   |
| 0.6137        | 3.0   | 21   | 0.7341          | 0.4286   |
| 0.3805        | 4.0   | 28   | 1.0217          | 0.4286   |
| 0.2201        | 5.0   | 35   | 1.1437          | 0.2857   |
| 0.0296        | 6.0   | 42   | 1.5997          | 0.4286   |
| 0.0103        | 7.0   | 49   | 2.6835          | 0.4286   |
| 0.0046        | 8.0   | 56   | 3.3521          | 0.4286   |
| 0.002         | 9.0   | 63   | 3.7846          | 0.4286   |
| 0.0017        | 10.0  | 70   | 4.0088          | 0.4286   |
| 0.0018        | 11.0  | 77   | 4.1483          | 0.4286   |
| 0.0006        | 12.0  | 84   | 4.2235          | 0.4286   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
