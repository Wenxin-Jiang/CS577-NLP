---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model_index:
- name: bert-srb-ner-setimes
  results:
  - task:
      name: Token Classification
      type: token-classification
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9645112274185379
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-srb-ner-setimes

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1955
- Precision: 0.8229
- Recall: 0.8465
- F1: 0.8345
- Accuracy: 0.9645

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
| No log        | 1.0   | 104  | 0.2281          | 0.6589    | 0.7001 | 0.6789 | 0.9350   |
| No log        | 2.0   | 208  | 0.1833          | 0.7105    | 0.7694 | 0.7388 | 0.9470   |
| No log        | 3.0   | 312  | 0.1573          | 0.7461    | 0.7778 | 0.7616 | 0.9525   |
| No log        | 4.0   | 416  | 0.1489          | 0.7665    | 0.8091 | 0.7872 | 0.9557   |
| 0.1898        | 5.0   | 520  | 0.1445          | 0.7881    | 0.8327 | 0.8098 | 0.9587   |
| 0.1898        | 6.0   | 624  | 0.1473          | 0.7913    | 0.8316 | 0.8109 | 0.9601   |
| 0.1898        | 7.0   | 728  | 0.1558          | 0.8101    | 0.8347 | 0.8222 | 0.9620   |
| 0.1898        | 8.0   | 832  | 0.1616          | 0.8026    | 0.8302 | 0.8162 | 0.9612   |
| 0.1898        | 9.0   | 936  | 0.1716          | 0.8127    | 0.8409 | 0.8266 | 0.9631   |
| 0.0393        | 10.0  | 1040 | 0.1751          | 0.8140    | 0.8369 | 0.8253 | 0.9628   |
| 0.0393        | 11.0  | 1144 | 0.1775          | 0.8096    | 0.8420 | 0.8255 | 0.9626   |
| 0.0393        | 12.0  | 1248 | 0.1763          | 0.8161    | 0.8386 | 0.8272 | 0.9636   |
| 0.0393        | 13.0  | 1352 | 0.1949          | 0.8259    | 0.8400 | 0.8329 | 0.9634   |
| 0.0393        | 14.0  | 1456 | 0.1842          | 0.8205    | 0.8420 | 0.8311 | 0.9642   |
| 0.0111        | 15.0  | 1560 | 0.1862          | 0.8160    | 0.8493 | 0.8323 | 0.9646   |
| 0.0111        | 16.0  | 1664 | 0.1989          | 0.8176    | 0.8367 | 0.8270 | 0.9627   |
| 0.0111        | 17.0  | 1768 | 0.1945          | 0.8246    | 0.8409 | 0.8327 | 0.9638   |
| 0.0111        | 18.0  | 1872 | 0.1997          | 0.8270    | 0.8426 | 0.8347 | 0.9634   |
| 0.0111        | 19.0  | 1976 | 0.1917          | 0.8258    | 0.8491 | 0.8373 | 0.9651   |
| 0.0051        | 20.0  | 2080 | 0.1955          | 0.8229    | 0.8465 | 0.8345 | 0.9645   |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0
- Datasets 1.11.0
- Tokenizers 0.10.1
