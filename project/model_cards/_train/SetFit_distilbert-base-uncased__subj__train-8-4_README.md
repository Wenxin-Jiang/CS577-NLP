---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-4

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3305
- Accuracy: 0.8565

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
| 0.6991        | 1.0   | 3    | 0.6772          | 0.75     |
| 0.6707        | 2.0   | 6    | 0.6704          | 0.75     |
| 0.6402        | 3.0   | 9    | 0.6608          | 1.0      |
| 0.5789        | 4.0   | 12   | 0.6547          | 0.75     |
| 0.5211        | 5.0   | 15   | 0.6434          | 0.75     |
| 0.454         | 6.0   | 18   | 0.6102          | 1.0      |
| 0.4187        | 7.0   | 21   | 0.5701          | 1.0      |
| 0.3401        | 8.0   | 24   | 0.5289          | 1.0      |
| 0.3107        | 9.0   | 27   | 0.4737          | 1.0      |
| 0.2381        | 10.0  | 30   | 0.4255          | 1.0      |
| 0.1982        | 11.0  | 33   | 0.3685          | 1.0      |
| 0.1631        | 12.0  | 36   | 0.3200          | 1.0      |
| 0.1234        | 13.0  | 39   | 0.2798          | 1.0      |
| 0.0993        | 14.0  | 42   | 0.2455          | 1.0      |
| 0.0781        | 15.0  | 45   | 0.2135          | 1.0      |
| 0.0586        | 16.0  | 48   | 0.1891          | 1.0      |
| 0.0513        | 17.0  | 51   | 0.1671          | 1.0      |
| 0.043         | 18.0  | 54   | 0.1427          | 1.0      |
| 0.0307        | 19.0  | 57   | 0.1225          | 1.0      |
| 0.0273        | 20.0  | 60   | 0.1060          | 1.0      |
| 0.0266        | 21.0  | 63   | 0.0920          | 1.0      |
| 0.0233        | 22.0  | 66   | 0.0823          | 1.0      |
| 0.0185        | 23.0  | 69   | 0.0751          | 1.0      |
| 0.0173        | 24.0  | 72   | 0.0698          | 1.0      |
| 0.0172        | 25.0  | 75   | 0.0651          | 1.0      |
| 0.0142        | 26.0  | 78   | 0.0613          | 1.0      |
| 0.0151        | 27.0  | 81   | 0.0583          | 1.0      |
| 0.0117        | 28.0  | 84   | 0.0563          | 1.0      |
| 0.0123        | 29.0  | 87   | 0.0546          | 1.0      |
| 0.0121        | 30.0  | 90   | 0.0531          | 1.0      |
| 0.0123        | 31.0  | 93   | 0.0511          | 1.0      |
| 0.0112        | 32.0  | 96   | 0.0496          | 1.0      |
| 0.0103        | 33.0  | 99   | 0.0481          | 1.0      |
| 0.0086        | 34.0  | 102  | 0.0468          | 1.0      |
| 0.0096        | 35.0  | 105  | 0.0457          | 1.0      |
| 0.0107        | 36.0  | 108  | 0.0447          | 1.0      |
| 0.0095        | 37.0  | 111  | 0.0439          | 1.0      |
| 0.0102        | 38.0  | 114  | 0.0429          | 1.0      |
| 0.0077        | 39.0  | 117  | 0.0422          | 1.0      |
| 0.0092        | 40.0  | 120  | 0.0415          | 1.0      |
| 0.0083        | 41.0  | 123  | 0.0409          | 1.0      |
| 0.0094        | 42.0  | 126  | 0.0404          | 1.0      |
| 0.0084        | 43.0  | 129  | 0.0400          | 1.0      |
| 0.0085        | 44.0  | 132  | 0.0396          | 1.0      |
| 0.0092        | 45.0  | 135  | 0.0392          | 1.0      |
| 0.0076        | 46.0  | 138  | 0.0389          | 1.0      |
| 0.0073        | 47.0  | 141  | 0.0388          | 1.0      |
| 0.0085        | 48.0  | 144  | 0.0387          | 1.0      |
| 0.0071        | 49.0  | 147  | 0.0386          | 1.0      |
| 0.0079        | 50.0  | 150  | 0.0386          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
