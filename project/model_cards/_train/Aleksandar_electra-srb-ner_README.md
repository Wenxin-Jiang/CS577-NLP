---
tags:
- generated_from_trainer
datasets:
- wikiann
metrics:
- precision
- recall
- f1
- accuracy
model_index:
- name: electra-srb-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      args: sr
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9568394937134688
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# electra-srb-ner

This model was trained from scratch on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3406
- Precision: 0.8934
- Recall: 0.9087
- F1: 0.9010
- Accuracy: 0.9568

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

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3686        | 1.0   | 625   | 0.2108          | 0.8326    | 0.8494 | 0.8409 | 0.9335   |
| 0.1886        | 2.0   | 1250  | 0.1784          | 0.8737    | 0.8713 | 0.8725 | 0.9456   |
| 0.1323        | 3.0   | 1875  | 0.1805          | 0.8654    | 0.8870 | 0.8760 | 0.9468   |
| 0.0675        | 4.0   | 2500  | 0.2018          | 0.8736    | 0.8880 | 0.8807 | 0.9502   |
| 0.0425        | 5.0   | 3125  | 0.2162          | 0.8818    | 0.8945 | 0.8881 | 0.9512   |
| 0.0343        | 6.0   | 3750  | 0.2492          | 0.8790    | 0.8928 | 0.8859 | 0.9513   |
| 0.0253        | 7.0   | 4375  | 0.2562          | 0.8821    | 0.9006 | 0.8912 | 0.9525   |
| 0.0142        | 8.0   | 5000  | 0.2788          | 0.8807    | 0.9013 | 0.8909 | 0.9524   |
| 0.0114        | 9.0   | 5625  | 0.2793          | 0.8861    | 0.9002 | 0.8931 | 0.9534   |
| 0.0095        | 10.0  | 6250  | 0.2967          | 0.8887    | 0.9034 | 0.8960 | 0.9550   |
| 0.008         | 11.0  | 6875  | 0.2993          | 0.8899    | 0.9067 | 0.8982 | 0.9556   |
| 0.0048        | 12.0  | 7500  | 0.3215          | 0.8887    | 0.9038 | 0.8962 | 0.9545   |
| 0.0034        | 13.0  | 8125  | 0.3242          | 0.8897    | 0.9068 | 0.8982 | 0.9554   |
| 0.003         | 14.0  | 8750  | 0.3311          | 0.8884    | 0.9085 | 0.8983 | 0.9559   |
| 0.0025        | 15.0  | 9375  | 0.3383          | 0.8943    | 0.9062 | 0.9002 | 0.9562   |
| 0.0011        | 16.0  | 10000 | 0.3346          | 0.8941    | 0.9112 | 0.9026 | 0.9574   |
| 0.0015        | 17.0  | 10625 | 0.3362          | 0.8944    | 0.9081 | 0.9012 | 0.9567   |
| 0.001         | 18.0  | 11250 | 0.3464          | 0.8877    | 0.9100 | 0.8987 | 0.9559   |
| 0.0012        | 19.0  | 11875 | 0.3415          | 0.8944    | 0.9089 | 0.9016 | 0.9568   |
| 0.0005        | 20.0  | 12500 | 0.3406          | 0.8934    | 0.9087 | 0.9010 | 0.9568   |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0
- Datasets 1.11.0
- Tokenizers 0.10.1
