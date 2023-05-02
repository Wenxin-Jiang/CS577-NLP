---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-tmvar-corpus
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-tmvar-corpus

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0002
- I F1: 1.0
- S F1: 1.0
- M F1: 0.9994
- P F1: 0.9994
- R F1: 1.0
- D F1: 1.0
- T F1: 1.0
- F F1: 1.0
- W F1: 0.9986
- A F1: 0.9977
- Precision: 0.9988
- Recall: 0.9997
- F1: 0.9993
- Accuracy: 1.0000

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | I F1   | S F1   | M F1   | P F1   | R F1   | D F1 | T F1   | F F1   | W F1   | A F1   | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:------:|:------:|:----:|:------:|:------:|:------:|:------:|:---------:|:------:|:------:|:--------:|
| 0.0364        | 1.0   | 454  | 0.0250          | 0.7336 | 0.0    | 0.8644 | 0.8347 | 0.9246 | 0.0  | 0.8854 | 0.0    | 0.9041 | 0.9774 | 0.8595    | 0.8618 | 0.8607 | 0.9927   |
| 0.0371        | 2.0   | 908  | 0.0132          | 0.7906 | 0.0    | 0.9410 | 0.8785 | 0.9947 | 0.0  | 0.9509 | 0.4118 | 0.9615 | 0.9931 | 0.9068    | 0.9236 | 0.9151 | 0.9960   |
| 0.0084        | 3.0   | 1362 | 0.0074          | 0.8591 | 0.8    | 0.9683 | 0.9585 | 0.9894 | 0.0  | 0.9677 | 0.8636 | 0.9719 | 0.9954 | 0.9463    | 0.9635 | 0.9548 | 0.9977   |
| 0.0034        | 4.0   | 1816 | 0.0040          | 0.9205 | 0.9412 | 0.9815 | 0.9735 | 1.0    | 0.8  | 0.9656 | 0.9778 | 0.9830 | 0.9977 | 0.9636    | 0.9818 | 0.9726 | 0.9987   |
| 0.0029        | 5.0   | 2270 | 0.0022          | 0.9623 | 0.9412 | 0.9864 | 0.9836 | 0.9947 | 0.8  | 0.9837 | 0.9333 | 0.9859 | 0.9977 | 0.9793    | 0.9865 | 0.9829 | 0.9992   |
| 0.003         | 6.0   | 2724 | 0.0024          | 0.9748 | 0.9412 | 0.9797 | 0.9789 | 1.0    | 0.8  | 0.9887 | 0.9333 | 0.9879 | 0.9954 | 0.9748    | 0.9903 | 0.9825 | 0.9991   |
| 0.0009        | 7.0   | 3178 | 0.0008          | 0.9874 | 1.0    | 0.9936 | 0.9951 | 1.0    | 1.0  | 0.9975 | 1.0    | 0.9936 | 0.9977 | 0.9927    | 0.9959 | 0.9943 | 0.9997   |
| 0.0002        | 8.0   | 3632 | 0.0004          | 1.0    | 1.0    | 0.9955 | 0.9976 | 1.0    | 1.0  | 0.9987 | 1.0    | 0.9964 | 0.9977 | 0.9956    | 0.9991 | 0.9974 | 0.9999   |
| 0.0004        | 9.0   | 4086 | 0.0003          | 1.0    | 1.0    | 0.9994 | 0.9994 | 1.0    | 1.0  | 1.0    | 1.0    | 0.9979 | 0.9977 | 0.9985    | 0.9997 | 0.9991 | 1.0000   |
| 0.0007        | 10.0  | 4540 | 0.0002          | 1.0    | 1.0    | 0.9994 | 0.9994 | 1.0    | 1.0  | 1.0    | 1.0    | 0.9986 | 0.9977 | 0.9988    | 0.9997 | 0.9993 | 1.0000   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.12.1
