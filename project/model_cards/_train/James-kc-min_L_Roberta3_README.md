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
- name: L_Roberta3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# L_Roberta3

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2095
- Accuracy: 0.9555
- F1: 0.9555
- Precision: 0.9555
- Recall: 0.9555
- C Report:               precision    recall  f1-score   support

           0       0.97      0.95      0.96       876
           1       0.94      0.97      0.95       696

    accuracy                           0.96      1572
   macro avg       0.95      0.96      0.96      1572
weighted avg       0.96      0.96      0.96      1572

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
| 0.2674        | 1.0   | 329  | 0.2436          | 0.9389   | 0.9389 | 0.9389    | 0.9389 |               precision    recall  f1-score   support

           0       0.94      0.95      0.95       876
           1       0.94      0.92      0.93       696

    accuracy                           0.94      1572
   macro avg       0.94      0.94      0.94      1572
weighted avg       0.94      0.94      0.94      1572
 | None     |
| 0.1377        | 2.0   | 658  | 0.1506          | 0.9408   | 0.9408 | 0.9408    | 0.9408 |               precision    recall  f1-score   support

           0       0.97      0.92      0.95       876
           1       0.91      0.96      0.94       696

    accuracy                           0.94      1572
   macro avg       0.94      0.94      0.94      1572
weighted avg       0.94      0.94      0.94      1572
 | None     |
| 0.0898        | 3.0   | 987  | 0.1491          | 0.9548   | 0.9548 | 0.9548    | 0.9548 |               precision    recall  f1-score   support

           0       0.96      0.96      0.96       876
           1       0.95      0.95      0.95       696

    accuracy                           0.95      1572
   macro avg       0.95      0.95      0.95      1572
weighted avg       0.95      0.95      0.95      1572
 | None     |
| 0.0543        | 4.0   | 1316 | 0.1831          | 0.9561   | 0.9561 | 0.9561    | 0.9561 |               precision    recall  f1-score   support

           0       0.97      0.95      0.96       876
           1       0.94      0.96      0.95       696

    accuracy                           0.96      1572
   macro avg       0.95      0.96      0.96      1572
weighted avg       0.96      0.96      0.96      1572
 | None     |
| 0.0394        | 5.0   | 1645 | 0.2095          | 0.9555   | 0.9555 | 0.9555    | 0.9555 |               precision    recall  f1-score   support

           0       0.97      0.95      0.96       876
           1       0.94      0.97      0.95       696

    accuracy                           0.96      1572
   macro avg       0.95      0.96      0.96      1572
weighted avg       0.96      0.96      0.96      1572
 | None     |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.2+cu102
- Datasets 2.2.2
- Tokenizers 0.12.1
