---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model_index:
- name: electra-srb-ner-setimes
  results:
  - task:
      name: Token Classification
      type: token-classification
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9546789604788638
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# electra-srb-ner-setimes

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2804
- Precision: 0.8286
- Recall: 0.8081
- F1: 0.8182
- Accuracy: 0.9547

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 104  | 0.2981          | 0.6737    | 0.6113 | 0.6410 | 0.9174   |
| No log        | 2.0   | 208  | 0.2355          | 0.7279    | 0.6701 | 0.6978 | 0.9307   |
| No log        | 3.0   | 312  | 0.2079          | 0.7707    | 0.7062 | 0.7371 | 0.9402   |
| No log        | 4.0   | 416  | 0.2078          | 0.7689    | 0.7479 | 0.7582 | 0.9449   |
| 0.2391        | 5.0   | 520  | 0.2089          | 0.8083    | 0.7476 | 0.7767 | 0.9484   |
| 0.2391        | 6.0   | 624  | 0.2199          | 0.7981    | 0.7726 | 0.7851 | 0.9487   |
| 0.2391        | 7.0   | 728  | 0.2528          | 0.8205    | 0.7749 | 0.7971 | 0.9511   |
| 0.2391        | 8.0   | 832  | 0.2265          | 0.8074    | 0.8003 | 0.8038 | 0.9524   |
| 0.2391        | 9.0   | 936  | 0.2843          | 0.8265    | 0.7716 | 0.7981 | 0.9504   |
| 0.0378        | 10.0  | 1040 | 0.2450          | 0.8024    | 0.8019 | 0.8021 | 0.9520   |
| 0.0378        | 11.0  | 1144 | 0.2550          | 0.8116    | 0.7986 | 0.8051 | 0.9519   |
| 0.0378        | 12.0  | 1248 | 0.2706          | 0.8208    | 0.7957 | 0.8081 | 0.9532   |
| 0.0378        | 13.0  | 1352 | 0.2664          | 0.8040    | 0.8035 | 0.8038 | 0.9530   |
| 0.0378        | 14.0  | 1456 | 0.2571          | 0.8011    | 0.8110 | 0.8060 | 0.9529   |
| 0.0099        | 15.0  | 1560 | 0.2673          | 0.8051    | 0.8129 | 0.8090 | 0.9534   |
| 0.0099        | 16.0  | 1664 | 0.2733          | 0.8074    | 0.8087 | 0.8081 | 0.9529   |
| 0.0099        | 17.0  | 1768 | 0.2835          | 0.8254    | 0.8074 | 0.8163 | 0.9543   |
| 0.0099        | 18.0  | 1872 | 0.2771          | 0.8222    | 0.8081 | 0.8151 | 0.9545   |
| 0.0099        | 19.0  | 1976 | 0.2776          | 0.8237    | 0.8084 | 0.8160 | 0.9546   |
| 0.0044        | 20.0  | 2080 | 0.2804          | 0.8286    | 0.8081 | 0.8182 | 0.9547   |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0
- Datasets 1.11.0
- Tokenizers 0.10.1
