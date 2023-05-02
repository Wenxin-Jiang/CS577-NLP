---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-0

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9917
- Accuracy: 0.7705

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
| 0.7001        | 1.0   | 7    | 0.7327          | 0.2857   |
| 0.6326        | 2.0   | 14   | 0.6479          | 0.5714   |
| 0.5232        | 3.0   | 21   | 0.5714          | 0.5714   |
| 0.3313        | 4.0   | 28   | 0.6340          | 0.7143   |
| 0.3161        | 5.0   | 35   | 0.6304          | 0.7143   |
| 0.0943        | 6.0   | 42   | 0.4719          | 0.8571   |
| 0.0593        | 7.0   | 49   | 0.5000          | 0.7143   |
| 0.0402        | 8.0   | 56   | 0.3530          | 0.8571   |
| 0.0307        | 9.0   | 63   | 0.3499          | 0.8571   |
| 0.0033        | 10.0  | 70   | 0.3258          | 0.8571   |
| 0.0021        | 11.0  | 77   | 0.3362          | 0.8571   |
| 0.0012        | 12.0  | 84   | 0.4591          | 0.8571   |
| 0.0036        | 13.0  | 91   | 0.4661          | 0.8571   |
| 0.001         | 14.0  | 98   | 0.5084          | 0.8571   |
| 0.0017        | 15.0  | 105  | 0.5844          | 0.8571   |
| 0.0005        | 16.0  | 112  | 0.6645          | 0.8571   |
| 0.002         | 17.0  | 119  | 0.7422          | 0.8571   |
| 0.0006        | 18.0  | 126  | 0.7354          | 0.8571   |
| 0.0005        | 19.0  | 133  | 0.7265          | 0.8571   |
| 0.0005        | 20.0  | 140  | 0.7207          | 0.8571   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
