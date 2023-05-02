---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: F_Roberta_classifier2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# F_Roberta_classifier2

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1317
- Accuracy: 0.9751
- F1: 0.9751
- Precision: 0.9751
- Recall: 0.9751
- C Report:               precision    recall  f1-score   support

           0       0.97      0.98      0.98      1467
           1       0.98      0.97      0.98      1466

    accuracy                           0.98      2933
   macro avg       0.98      0.98      0.98      2933
weighted avg       0.98      0.98      0.98      2933

- C Matrix: None

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall | C Report                                                                                                                                                                                                                                                                                                                               | C Matrix |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|
| 0.1626        | 1.0   | 614  | 0.0936          | 0.9707   | 0.9707 | 0.9707    | 0.9707 |               precision    recall  f1-score   support

           0       0.97      0.97      0.97      1467
           1       0.97      0.97      0.97      1466

    accuracy                           0.97      2933
   macro avg       0.97      0.97      0.97      2933
weighted avg       0.97      0.97      0.97      2933
 | None     |
| 0.0827        | 2.0   | 1228 | 0.0794          | 0.9731   | 0.9731 | 0.9731    | 0.9731 |               precision    recall  f1-score   support

           0       0.96      0.98      0.97      1467
           1       0.98      0.96      0.97      1466

    accuracy                           0.97      2933
   macro avg       0.97      0.97      0.97      2933
weighted avg       0.97      0.97      0.97      2933
 | None     |
| 0.0525        | 3.0   | 1842 | 0.1003          | 0.9737   | 0.9737 | 0.9737    | 0.9737 |               precision    recall  f1-score   support

           0       0.97      0.98      0.97      1467
           1       0.98      0.97      0.97      1466

    accuracy                           0.97      2933
   macro avg       0.97      0.97      0.97      2933
weighted avg       0.97      0.97      0.97      2933
 | None     |
| 0.0329        | 4.0   | 2456 | 0.1184          | 0.9751   | 0.9751 | 0.9751    | 0.9751 |               precision    recall  f1-score   support

           0       0.98      0.97      0.98      1467
           1       0.97      0.98      0.98      1466

    accuracy                           0.98      2933
   macro avg       0.98      0.98      0.98      2933
weighted avg       0.98      0.98      0.98      2933
 | None     |
| 0.0179        | 5.0   | 3070 | 0.1317          | 0.9751   | 0.9751 | 0.9751    | 0.9751 |               precision    recall  f1-score   support

           0       0.97      0.98      0.98      1467
           1       0.98      0.97      0.98      1466

    accuracy                           0.98      2933
   macro avg       0.98      0.98      0.98      2933
weighted avg       0.98      0.98      0.98      2933
 | None     |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.2.0
- Tokenizers 0.12.1
