---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-base-multilingual-cased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0379
- Precision: 0.9706
- Recall: 0.9753
- F1: 0.9729
- Accuracy: 0.9918

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0683        | 1.0   | 963  | 0.0550          | 0.9367    | 0.9505 | 0.9435 | 0.9839   |
| 0.0211        | 2.0   | 1926 | 0.0428          | 0.9580    | 0.9735 | 0.9657 | 0.9902   |
| 0.0098        | 3.0   | 2889 | 0.0379          | 0.9706    | 0.9753 | 0.9729 | 0.9918   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
