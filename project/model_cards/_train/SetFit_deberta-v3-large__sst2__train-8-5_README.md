---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-5

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3078
- Accuracy: 0.6930

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
| 0.6813        | 1.0   | 3    | 0.7842          | 0.25     |
| 0.6617        | 2.0   | 6    | 0.7968          | 0.25     |
| 0.6945        | 3.0   | 9    | 0.7746          | 0.25     |
| 0.5967        | 4.0   | 12   | 0.7557          | 0.25     |
| 0.4824        | 5.0   | 15   | 0.6920          | 0.25     |
| 0.3037        | 6.0   | 18   | 0.6958          | 0.5      |
| 0.2329        | 7.0   | 21   | 0.6736          | 0.5      |
| 0.1441        | 8.0   | 24   | 0.3749          | 1.0      |
| 0.0875        | 9.0   | 27   | 0.3263          | 0.75     |
| 0.0655        | 10.0  | 30   | 0.3525          | 0.75     |
| 0.0373        | 11.0  | 33   | 0.1993          | 1.0      |
| 0.0173        | 12.0  | 36   | 0.1396          | 1.0      |
| 0.0147        | 13.0  | 39   | 0.0655          | 1.0      |
| 0.0084        | 14.0  | 42   | 0.0343          | 1.0      |
| 0.0049        | 15.0  | 45   | 0.0225          | 1.0      |
| 0.004         | 16.0  | 48   | 0.0167          | 1.0      |
| 0.003         | 17.0  | 51   | 0.0134          | 1.0      |
| 0.0027        | 18.0  | 54   | 0.0114          | 1.0      |
| 0.002         | 19.0  | 57   | 0.0104          | 1.0      |
| 0.0015        | 20.0  | 60   | 0.0099          | 1.0      |
| 0.0014        | 21.0  | 63   | 0.0095          | 1.0      |
| 0.0013        | 22.0  | 66   | 0.0095          | 1.0      |
| 0.0012        | 23.0  | 69   | 0.0091          | 1.0      |
| 0.0011        | 24.0  | 72   | 0.0085          | 1.0      |
| 0.0009        | 25.0  | 75   | 0.0081          | 1.0      |
| 0.001         | 26.0  | 78   | 0.0077          | 1.0      |
| 0.0008        | 27.0  | 81   | 0.0074          | 1.0      |
| 0.0009        | 28.0  | 84   | 0.0071          | 1.0      |
| 0.0007        | 29.0  | 87   | 0.0068          | 1.0      |
| 0.0008        | 30.0  | 90   | 0.0064          | 1.0      |
| 0.0007        | 31.0  | 93   | 0.0062          | 1.0      |
| 0.0007        | 32.0  | 96   | 0.0059          | 1.0      |
| 0.0007        | 33.0  | 99   | 0.0056          | 1.0      |
| 0.0005        | 34.0  | 102  | 0.0054          | 1.0      |
| 0.0006        | 35.0  | 105  | 0.0053          | 1.0      |
| 0.0008        | 36.0  | 108  | 0.0051          | 1.0      |
| 0.0007        | 37.0  | 111  | 0.0050          | 1.0      |
| 0.0007        | 38.0  | 114  | 0.0049          | 1.0      |
| 0.0006        | 39.0  | 117  | 0.0048          | 1.0      |
| 0.0005        | 40.0  | 120  | 0.0048          | 1.0      |
| 0.0005        | 41.0  | 123  | 0.0048          | 1.0      |
| 0.0005        | 42.0  | 126  | 0.0047          | 1.0      |
| 0.0005        | 43.0  | 129  | 0.0047          | 1.0      |
| 0.0005        | 44.0  | 132  | 0.0047          | 1.0      |
| 0.0006        | 45.0  | 135  | 0.0047          | 1.0      |
| 0.0005        | 46.0  | 138  | 0.0047          | 1.0      |
| 0.0005        | 47.0  | 141  | 0.0047          | 1.0      |
| 0.0006        | 48.0  | 144  | 0.0047          | 1.0      |
| 0.0005        | 49.0  | 147  | 0.0047          | 1.0      |
| 0.0005        | 50.0  | 150  | 0.0047          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
