---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-6

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8356
- Accuracy: 0.6480

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
| 0.6978        | 1.0   | 7    | 0.6807          | 0.4286   |
| 0.6482        | 2.0   | 14   | 0.6775          | 0.4286   |
| 0.6051        | 3.0   | 21   | 0.6623          | 0.5714   |
| 0.486         | 4.0   | 28   | 0.6710          | 0.5714   |
| 0.4612        | 5.0   | 35   | 0.5325          | 0.7143   |
| 0.2233        | 6.0   | 42   | 0.4992          | 0.7143   |
| 0.1328        | 7.0   | 49   | 0.4753          | 0.7143   |
| 0.0905        | 8.0   | 56   | 0.2416          | 1.0      |
| 0.0413        | 9.0   | 63   | 0.2079          | 1.0      |
| 0.0356        | 10.0  | 70   | 0.2234          | 0.8571   |
| 0.0217        | 11.0  | 77   | 0.2639          | 0.8571   |
| 0.0121        | 12.0  | 84   | 0.2977          | 0.8571   |
| 0.0105        | 13.0  | 91   | 0.3468          | 0.8571   |
| 0.0085        | 14.0  | 98   | 0.3912          | 0.8571   |
| 0.0077        | 15.0  | 105  | 0.4000          | 0.8571   |
| 0.0071        | 16.0  | 112  | 0.4015          | 0.8571   |
| 0.0078        | 17.0  | 119  | 0.3865          | 0.8571   |
| 0.0059        | 18.0  | 126  | 0.3603          | 0.8571   |
| 0.0051        | 19.0  | 133  | 0.3231          | 0.8571   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
