---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-6

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4331
- Accuracy: 0.7106

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
| 0.6486        | 1.0   | 3    | 0.7901          | 0.25     |
| 0.6418        | 2.0   | 6    | 0.9259          | 0.25     |
| 0.6169        | 3.0   | 9    | 1.0574          | 0.25     |
| 0.5639        | 4.0   | 12   | 1.1372          | 0.25     |
| 0.4562        | 5.0   | 15   | 0.6090          | 0.5      |
| 0.3105        | 6.0   | 18   | 0.4435          | 1.0      |
| 0.2303        | 7.0   | 21   | 0.2804          | 1.0      |
| 0.1388        | 8.0   | 24   | 0.2205          | 1.0      |
| 0.0918        | 9.0   | 27   | 0.1282          | 1.0      |
| 0.0447        | 10.0  | 30   | 0.0643          | 1.0      |
| 0.0297        | 11.0  | 33   | 0.0361          | 1.0      |
| 0.0159        | 12.0  | 36   | 0.0211          | 1.0      |
| 0.0102        | 13.0  | 39   | 0.0155          | 1.0      |
| 0.0061        | 14.0  | 42   | 0.0158          | 1.0      |
| 0.0049        | 15.0  | 45   | 0.0189          | 1.0      |
| 0.0035        | 16.0  | 48   | 0.0254          | 1.0      |
| 0.0027        | 17.0  | 51   | 0.0305          | 1.0      |
| 0.0021        | 18.0  | 54   | 0.0287          | 1.0      |
| 0.0016        | 19.0  | 57   | 0.0215          | 1.0      |
| 0.0016        | 20.0  | 60   | 0.0163          | 1.0      |
| 0.0014        | 21.0  | 63   | 0.0138          | 1.0      |
| 0.0015        | 22.0  | 66   | 0.0131          | 1.0      |
| 0.001         | 23.0  | 69   | 0.0132          | 1.0      |
| 0.0014        | 24.0  | 72   | 0.0126          | 1.0      |
| 0.0011        | 25.0  | 75   | 0.0125          | 1.0      |
| 0.001         | 26.0  | 78   | 0.0119          | 1.0      |
| 0.0008        | 27.0  | 81   | 0.0110          | 1.0      |
| 0.0007        | 28.0  | 84   | 0.0106          | 1.0      |
| 0.0008        | 29.0  | 87   | 0.0095          | 1.0      |
| 0.0009        | 30.0  | 90   | 0.0089          | 1.0      |
| 0.0008        | 31.0  | 93   | 0.0083          | 1.0      |
| 0.0007        | 32.0  | 96   | 0.0075          | 1.0      |
| 0.0008        | 33.0  | 99   | 0.0066          | 1.0      |
| 0.0006        | 34.0  | 102  | 0.0059          | 1.0      |
| 0.0007        | 35.0  | 105  | 0.0054          | 1.0      |
| 0.0008        | 36.0  | 108  | 0.0051          | 1.0      |
| 0.0007        | 37.0  | 111  | 0.0049          | 1.0      |
| 0.0007        | 38.0  | 114  | 0.0047          | 1.0      |
| 0.0006        | 39.0  | 117  | 0.0045          | 1.0      |
| 0.0006        | 40.0  | 120  | 0.0046          | 1.0      |
| 0.0005        | 41.0  | 123  | 0.0045          | 1.0      |
| 0.0006        | 42.0  | 126  | 0.0044          | 1.0      |
| 0.0006        | 43.0  | 129  | 0.0043          | 1.0      |
| 0.0006        | 44.0  | 132  | 0.0044          | 1.0      |
| 0.0005        | 45.0  | 135  | 0.0045          | 1.0      |
| 0.0006        | 46.0  | 138  | 0.0043          | 1.0      |
| 0.0006        | 47.0  | 141  | 0.0043          | 1.0      |
| 0.0006        | 48.0  | 144  | 0.0041          | 1.0      |
| 0.0007        | 49.0  | 147  | 0.0042          | 1.0      |
| 0.0005        | 50.0  | 150  | 0.0042          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
