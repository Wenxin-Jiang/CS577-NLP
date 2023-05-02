---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-8-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-8-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8419
- Accuracy: 0.6172

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
| 0.7057        | 1.0   | 3    | 0.6848          | 0.75     |
| 0.6681        | 2.0   | 6    | 0.6875          | 0.5      |
| 0.6591        | 3.0   | 9    | 0.6868          | 0.25     |
| 0.6052        | 4.0   | 12   | 0.6943          | 0.25     |
| 0.557         | 5.0   | 15   | 0.7078          | 0.25     |
| 0.4954        | 6.0   | 18   | 0.7168          | 0.25     |
| 0.4593        | 7.0   | 21   | 0.7185          | 0.25     |
| 0.3936        | 8.0   | 24   | 0.7212          | 0.25     |
| 0.3699        | 9.0   | 27   | 0.6971          | 0.5      |
| 0.2916        | 10.0  | 30   | 0.6827          | 0.5      |
| 0.2511        | 11.0  | 33   | 0.6464          | 0.5      |
| 0.2109        | 12.0  | 36   | 0.6344          | 0.75     |
| 0.1655        | 13.0  | 39   | 0.6377          | 0.75     |
| 0.1412        | 14.0  | 42   | 0.6398          | 0.75     |
| 0.1157        | 15.0  | 45   | 0.6315          | 0.75     |
| 0.0895        | 16.0  | 48   | 0.6210          | 0.75     |
| 0.0783        | 17.0  | 51   | 0.5918          | 0.75     |
| 0.0606        | 18.0  | 54   | 0.5543          | 0.75     |
| 0.0486        | 19.0  | 57   | 0.5167          | 0.75     |
| 0.0405        | 20.0  | 60   | 0.4862          | 0.75     |
| 0.0376        | 21.0  | 63   | 0.4644          | 0.75     |
| 0.0294        | 22.0  | 66   | 0.4497          | 0.75     |
| 0.0261        | 23.0  | 69   | 0.4428          | 0.75     |
| 0.0238        | 24.0  | 72   | 0.4408          | 0.75     |
| 0.0217        | 25.0  | 75   | 0.4392          | 0.75     |
| 0.0187        | 26.0  | 78   | 0.4373          | 0.75     |
| 0.0177        | 27.0  | 81   | 0.4360          | 0.75     |
| 0.0136        | 28.0  | 84   | 0.4372          | 0.75     |
| 0.0144        | 29.0  | 87   | 0.4368          | 0.75     |
| 0.014         | 30.0  | 90   | 0.4380          | 0.75     |
| 0.0137        | 31.0  | 93   | 0.4383          | 0.75     |
| 0.0133        | 32.0  | 96   | 0.4409          | 0.75     |
| 0.013         | 33.0  | 99   | 0.4380          | 0.75     |
| 0.0096        | 34.0  | 102  | 0.4358          | 0.75     |
| 0.012         | 35.0  | 105  | 0.4339          | 0.75     |
| 0.0122        | 36.0  | 108  | 0.4305          | 0.75     |
| 0.0109        | 37.0  | 111  | 0.4267          | 0.75     |
| 0.0121        | 38.0  | 114  | 0.4231          | 0.75     |
| 0.0093        | 39.0  | 117  | 0.4209          | 0.75     |
| 0.0099        | 40.0  | 120  | 0.4199          | 0.75     |
| 0.0091        | 41.0  | 123  | 0.4184          | 0.75     |
| 0.0116        | 42.0  | 126  | 0.4173          | 0.75     |
| 0.01          | 43.0  | 129  | 0.4163          | 0.75     |
| 0.0098        | 44.0  | 132  | 0.4153          | 0.75     |
| 0.0101        | 45.0  | 135  | 0.4155          | 0.75     |
| 0.0088        | 46.0  | 138  | 0.4149          | 0.75     |
| 0.0087        | 47.0  | 141  | 0.4150          | 0.75     |
| 0.0093        | 48.0  | 144  | 0.4147          | 0.75     |
| 0.0081        | 49.0  | 147  | 0.4147          | 0.75     |
| 0.009         | 50.0  | 150  | 0.4150          | 0.75     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
