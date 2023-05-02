---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7887
- Accuracy: 0.6458

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
| 0.6928        | 1.0   | 7    | 0.6973          | 0.4286   |
| 0.675         | 2.0   | 14   | 0.7001          | 0.4286   |
| 0.6513        | 3.0   | 21   | 0.6959          | 0.4286   |
| 0.5702        | 4.0   | 28   | 0.6993          | 0.4286   |
| 0.5389        | 5.0   | 35   | 0.6020          | 0.7143   |
| 0.3386        | 6.0   | 42   | 0.5326          | 0.5714   |
| 0.2596        | 7.0   | 49   | 0.4943          | 0.7143   |
| 0.1633        | 8.0   | 56   | 0.3589          | 0.8571   |
| 0.1086        | 9.0   | 63   | 0.2924          | 0.8571   |
| 0.0641        | 10.0  | 70   | 0.2687          | 0.8571   |
| 0.0409        | 11.0  | 77   | 0.2202          | 0.8571   |
| 0.0181        | 12.0  | 84   | 0.2445          | 0.8571   |
| 0.0141        | 13.0  | 91   | 0.2885          | 0.8571   |
| 0.0108        | 14.0  | 98   | 0.3069          | 0.8571   |
| 0.009         | 15.0  | 105  | 0.3006          | 0.8571   |
| 0.0084        | 16.0  | 112  | 0.2834          | 0.8571   |
| 0.0088        | 17.0  | 119  | 0.2736          | 0.8571   |
| 0.0062        | 18.0  | 126  | 0.2579          | 0.8571   |
| 0.0058        | 19.0  | 133  | 0.2609          | 0.8571   |
| 0.0057        | 20.0  | 140  | 0.2563          | 0.8571   |
| 0.0049        | 21.0  | 147  | 0.2582          | 0.8571   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
