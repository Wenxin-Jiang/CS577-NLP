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
- name: bert-srb-ner
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
      value: 0.9546696220907545
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-srb-ner

This model was trained from scratch on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3561
- Precision: 0.8909
- Recall: 0.9082
- F1: 0.8995
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

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3907        | 1.0   | 625   | 0.2316          | 0.8255    | 0.8314 | 0.8285 | 0.9259   |
| 0.2091        | 2.0   | 1250  | 0.1920          | 0.8598    | 0.8731 | 0.8664 | 0.9420   |
| 0.1562        | 3.0   | 1875  | 0.1833          | 0.8608    | 0.8820 | 0.8713 | 0.9441   |
| 0.0919        | 4.0   | 2500  | 0.1985          | 0.8712    | 0.8886 | 0.8798 | 0.9476   |
| 0.0625        | 5.0   | 3125  | 0.2195          | 0.8762    | 0.8923 | 0.8842 | 0.9485   |
| 0.0545        | 6.0   | 3750  | 0.2320          | 0.8706    | 0.9004 | 0.8852 | 0.9495   |
| 0.0403        | 7.0   | 4375  | 0.2459          | 0.8817    | 0.8957 | 0.8887 | 0.9505   |
| 0.0269        | 8.0   | 5000  | 0.2603          | 0.8813    | 0.9021 | 0.8916 | 0.9516   |
| 0.0193        | 9.0   | 5625  | 0.2916          | 0.8812    | 0.8949 | 0.8880 | 0.9500   |
| 0.0162        | 10.0  | 6250  | 0.2938          | 0.8814    | 0.9025 | 0.8918 | 0.9520   |
| 0.0134        | 11.0  | 6875  | 0.3330          | 0.8809    | 0.8961 | 0.8885 | 0.9497   |
| 0.0076        | 12.0  | 7500  | 0.3141          | 0.8840    | 0.9025 | 0.8932 | 0.9524   |
| 0.0069        | 13.0  | 8125  | 0.3292          | 0.8819    | 0.9065 | 0.8940 | 0.9535   |
| 0.0053        | 14.0  | 8750  | 0.3454          | 0.8844    | 0.9018 | 0.8930 | 0.9523   |
| 0.0038        | 15.0  | 9375  | 0.3519          | 0.8912    | 0.9061 | 0.8986 | 0.9539   |
| 0.0034        | 16.0  | 10000 | 0.3437          | 0.8894    | 0.9038 | 0.8965 | 0.9539   |
| 0.0024        | 17.0  | 10625 | 0.3518          | 0.8896    | 0.9072 | 0.8983 | 0.9543   |
| 0.0018        | 18.0  | 11250 | 0.3572          | 0.8877    | 0.9072 | 0.8973 | 0.9543   |
| 0.0015        | 19.0  | 11875 | 0.3554          | 0.8910    | 0.9081 | 0.8994 | 0.9549   |
| 0.0011        | 20.0  | 12500 | 0.3561          | 0.8909    | 0.9082 | 0.8995 | 0.9547   |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0
- Datasets 1.11.0
- Tokenizers 0.10.1
