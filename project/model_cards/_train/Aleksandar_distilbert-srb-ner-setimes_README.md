---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model_index:
- name: distilbert-srb-ner-setimes
  results:
  - task:
      name: Token Classification
      type: token-classification
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9665376552169005
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-srb-ner-setimes

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1838
- Precision: 0.8370
- Recall: 0.8617
- F1: 0.8492
- Accuracy: 0.9665

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
| No log        | 1.0   | 104  | 0.2319          | 0.6668    | 0.7029 | 0.6844 | 0.9358   |
| No log        | 2.0   | 208  | 0.1850          | 0.7265    | 0.7508 | 0.7385 | 0.9469   |
| No log        | 3.0   | 312  | 0.1584          | 0.7555    | 0.7937 | 0.7741 | 0.9538   |
| No log        | 4.0   | 416  | 0.1484          | 0.7644    | 0.8128 | 0.7879 | 0.9571   |
| 0.1939        | 5.0   | 520  | 0.1383          | 0.7850    | 0.8131 | 0.7988 | 0.9604   |
| 0.1939        | 6.0   | 624  | 0.1409          | 0.7914    | 0.8359 | 0.8130 | 0.9632   |
| 0.1939        | 7.0   | 728  | 0.1526          | 0.8176    | 0.8392 | 0.8283 | 0.9637   |
| 0.1939        | 8.0   | 832  | 0.1536          | 0.8195    | 0.8409 | 0.8301 | 0.9641   |
| 0.1939        | 9.0   | 936  | 0.1538          | 0.8242    | 0.8523 | 0.8380 | 0.9661   |
| 0.0364        | 10.0  | 1040 | 0.1612          | 0.8228    | 0.8413 | 0.8319 | 0.9652   |
| 0.0364        | 11.0  | 1144 | 0.1721          | 0.8289    | 0.8503 | 0.8395 | 0.9656   |
| 0.0364        | 12.0  | 1248 | 0.1645          | 0.8301    | 0.8590 | 0.8443 | 0.9663   |
| 0.0364        | 13.0  | 1352 | 0.1747          | 0.8352    | 0.8540 | 0.8445 | 0.9665   |
| 0.0364        | 14.0  | 1456 | 0.1703          | 0.8277    | 0.8573 | 0.8422 | 0.9663   |
| 0.011         | 15.0  | 1560 | 0.1770          | 0.8314    | 0.8624 | 0.8466 | 0.9665   |
| 0.011         | 16.0  | 1664 | 0.1903          | 0.8399    | 0.8537 | 0.8467 | 0.9661   |
| 0.011         | 17.0  | 1768 | 0.1837          | 0.8363    | 0.8590 | 0.8475 | 0.9665   |
| 0.011         | 18.0  | 1872 | 0.1820          | 0.8338    | 0.8570 | 0.8453 | 0.9667   |
| 0.011         | 19.0  | 1976 | 0.1855          | 0.8382    | 0.8620 | 0.8499 | 0.9666   |
| 0.0053        | 20.0  | 2080 | 0.1838          | 0.8370    | 0.8617 | 0.8492 | 0.9665   |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0
- Datasets 1.11.0
- Tokenizers 0.10.1
