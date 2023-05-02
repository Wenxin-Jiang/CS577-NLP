---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-4

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3023
- Accuracy: 0.7057

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
| 0.6816        | 1.0   | 3    | 0.8072          | 0.25     |
| 0.6672        | 2.0   | 6    | 0.8740          | 0.25     |
| 0.6667        | 3.0   | 9    | 0.8578          | 0.25     |
| 0.5346        | 4.0   | 12   | 1.0353          | 0.25     |
| 0.4517        | 5.0   | 15   | 1.1030          | 0.25     |
| 0.3095        | 6.0   | 18   | 0.9986          | 0.25     |
| 0.2464        | 7.0   | 21   | 0.9286          | 0.5      |
| 0.1342        | 8.0   | 24   | 0.4063          | 1.0      |
| 0.0851        | 9.0   | 27   | 0.2210          | 1.0      |
| 0.0491        | 10.0  | 30   | 0.2302          | 1.0      |
| 0.0211        | 11.0  | 33   | 0.4020          | 0.75     |
| 0.017         | 12.0  | 36   | 0.2382          | 1.0      |
| 0.0084        | 13.0  | 39   | 0.0852          | 1.0      |
| 0.0051        | 14.0  | 42   | 0.0354          | 1.0      |
| 0.0047        | 15.0  | 45   | 0.0208          | 1.0      |
| 0.0029        | 16.0  | 48   | 0.0155          | 1.0      |
| 0.0022        | 17.0  | 51   | 0.0139          | 1.0      |
| 0.0019        | 18.0  | 54   | 0.0144          | 1.0      |
| 0.0016        | 19.0  | 57   | 0.0168          | 1.0      |
| 0.0013        | 20.0  | 60   | 0.0231          | 1.0      |
| 0.0011        | 21.0  | 63   | 0.0369          | 1.0      |
| 0.0009        | 22.0  | 66   | 0.0528          | 1.0      |
| 0.001         | 23.0  | 69   | 0.0639          | 1.0      |
| 0.0009        | 24.0  | 72   | 0.0670          | 1.0      |
| 0.0009        | 25.0  | 75   | 0.0526          | 1.0      |
| 0.0008        | 26.0  | 78   | 0.0425          | 1.0      |
| 0.0011        | 27.0  | 81   | 0.0135          | 1.0      |
| 0.0007        | 28.0  | 84   | 0.0076          | 1.0      |
| 0.0007        | 29.0  | 87   | 0.0057          | 1.0      |
| 0.0007        | 30.0  | 90   | 0.0049          | 1.0      |
| 0.0008        | 31.0  | 93   | 0.0045          | 1.0      |
| 0.0007        | 32.0  | 96   | 0.0044          | 1.0      |
| 0.0008        | 33.0  | 99   | 0.0043          | 1.0      |
| 0.0005        | 34.0  | 102  | 0.0044          | 1.0      |
| 0.0006        | 35.0  | 105  | 0.0045          | 1.0      |
| 0.0006        | 36.0  | 108  | 0.0046          | 1.0      |
| 0.0007        | 37.0  | 111  | 0.0048          | 1.0      |
| 0.0006        | 38.0  | 114  | 0.0049          | 1.0      |
| 0.0005        | 39.0  | 117  | 0.0050          | 1.0      |
| 0.0005        | 40.0  | 120  | 0.0050          | 1.0      |
| 0.0004        | 41.0  | 123  | 0.0051          | 1.0      |
| 0.0005        | 42.0  | 126  | 0.0051          | 1.0      |
| 0.0004        | 43.0  | 129  | 0.0051          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
