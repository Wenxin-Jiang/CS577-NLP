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
language:
- sr
model_index:
- name: distilbert-srb-ner
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
      value: 0.9576561462374611
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-srb-ner

This model was trained from scratch on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2972
- Precision: 0.8871
- Recall: 0.9100
- F1: 0.8984
- Accuracy: 0.9577

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
| 0.3818        | 1.0   | 625   | 0.2175          | 0.8175    | 0.8370 | 0.8272 | 0.9306   |
| 0.198         | 2.0   | 1250  | 0.1766          | 0.8551    | 0.8732 | 0.8640 | 0.9458   |
| 0.1423        | 3.0   | 1875  | 0.1702          | 0.8597    | 0.8763 | 0.8679 | 0.9473   |
| 0.079         | 4.0   | 2500  | 0.1774          | 0.8674    | 0.8875 | 0.8773 | 0.9515   |
| 0.0531        | 5.0   | 3125  | 0.2011          | 0.8688    | 0.8965 | 0.8825 | 0.9522   |
| 0.0429        | 6.0   | 3750  | 0.2082          | 0.8769    | 0.8970 | 0.8868 | 0.9538   |
| 0.032         | 7.0   | 4375  | 0.2268          | 0.8764    | 0.8916 | 0.8839 | 0.9528   |
| 0.0204        | 8.0   | 5000  | 0.2423          | 0.8726    | 0.8959 | 0.8841 | 0.9529   |
| 0.0148        | 9.0   | 5625  | 0.2522          | 0.8774    | 0.8991 | 0.8881 | 0.9538   |
| 0.0125        | 10.0  | 6250  | 0.2544          | 0.8823    | 0.9024 | 0.8922 | 0.9559   |
| 0.0108        | 11.0  | 6875  | 0.2592          | 0.8780    | 0.9041 | 0.8909 | 0.9553   |
| 0.007         | 12.0  | 7500  | 0.2672          | 0.8877    | 0.9056 | 0.8965 | 0.9571   |
| 0.0048        | 13.0  | 8125  | 0.2714          | 0.8879    | 0.9089 | 0.8982 | 0.9583   |
| 0.0049        | 14.0  | 8750  | 0.2872          | 0.8873    | 0.9068 | 0.8970 | 0.9573   |
| 0.0034        | 15.0  | 9375  | 0.2915          | 0.8883    | 0.9114 | 0.8997 | 0.9577   |
| 0.0027        | 16.0  | 10000 | 0.2890          | 0.8865    | 0.9103 | 0.8983 | 0.9581   |
| 0.0028        | 17.0  | 10625 | 0.2885          | 0.8877    | 0.9085 | 0.8980 | 0.9576   |
| 0.0014        | 18.0  | 11250 | 0.2928          | 0.8860    | 0.9073 | 0.8965 | 0.9577   |
| 0.0013        | 19.0  | 11875 | 0.2963          | 0.8856    | 0.9099 | 0.8976 | 0.9576   |
| 0.001         | 20.0  | 12500 | 0.2972          | 0.8871    | 0.9100 | 0.8984 | 0.9577   |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0
- Datasets 1.11.0
- Tokenizers 0.10.1
