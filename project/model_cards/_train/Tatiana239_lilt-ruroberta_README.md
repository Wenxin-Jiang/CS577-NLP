---
tags:
- generated_from_trainer
model-index:
- name: lilt-ruroberta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lilt-ruroberta

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4919
- Comment: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 6}
- Date: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 3}
- Labname: {'precision': 0.5833333333333334, 'recall': 0.6666666666666666, 'f1': 0.6222222222222222, 'number': 21}
- Laboratory: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1}
- Measure: {'precision': 0.5833333333333334, 'recall': 0.7777777777777778, 'f1': 0.6666666666666666, 'number': 9}
- Ref Value: {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 8}
- Result: {'precision': 0.25, 'recall': 0.25, 'f1': 0.25, 'number': 12}
- Overall Precision: 0.4528
- Overall Recall: 0.4
- Overall F1: 0.4248
- Overall Accuracy: 0.8698

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 25
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Comment                                                   | Date                                                      | Labname                                                                                                 | Laboratory                                                | Measure                                                                                                | Ref Value                                                 | Result                                                                                     | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------------------------------------------------------:|:---------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------:|:------------------------------------------------------------------------------------------:|:-----------------:|:--------------:|:----------:|:----------------:|
| 2.4398        | 5.0   | 5    | 1.5928          | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 6} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 3} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 21}                                              | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 9}                                              | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 8} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 12}                                 | 0.0               | 0.0            | 0.0        | 0.5850           |
| 1.4788        | 10.0  | 10   | 1.1857          | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 6} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 3} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 21}                                              | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 9}                                              | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 8} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 12}                                 | 0.0               | 0.0            | 0.0        | 0.6512           |
| 0.9806        | 15.0  | 15   | 0.8188          | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 6} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 3} | {'precision': 0.21875, 'recall': 0.3333333333333333, 'f1': 0.2641509433962264, 'number': 21}            | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1} | {'precision': 0.5, 'recall': 0.1111111111111111, 'f1': 0.1818181818181818, 'number': 9}                | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 8} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 12}                                 | 0.1667            | 0.1333         | 0.1481     | 0.7660           |
| 0.6358        | 20.0  | 20   | 0.5763          | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 6} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 3} | {'precision': 0.41935483870967744, 'recall': 0.6190476190476191, 'f1': 0.5, 'number': 21}               | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1} | {'precision': 0.7, 'recall': 0.7777777777777778, 'f1': 0.7368421052631577, 'number': 9}                | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 8} | {'precision': 0.42857142857142855, 'recall': 0.25, 'f1': 0.3157894736842105, 'number': 12} | 0.4182            | 0.3833         | 0.4        | 0.8675           |
| 0.4712        | 25.0  | 25   | 0.4919          | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 6} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 3} | {'precision': 0.5833333333333334, 'recall': 0.6666666666666666, 'f1': 0.6222222222222222, 'number': 21} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1} | {'precision': 0.5833333333333334, 'recall': 0.7777777777777778, 'f1': 0.6666666666666666, 'number': 9} | {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 8} | {'precision': 0.25, 'recall': 0.25, 'f1': 0.25, 'number': 12}                              | 0.4528            | 0.4            | 0.4248     | 0.8698           |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.8.0
- Tokenizers 0.13.2
