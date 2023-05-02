---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: this_is_my_model
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.8673816819884236
    - name: Recall
      type: recall
      value: 0.9020892351274787
    - name: F1
      type: f1
      value: 0.884395070300295
    - name: Accuracy
      type: accuracy
      value: 0.9761756784752434
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# this_is_my_model

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1143
- Precision: 0.8674
- Recall: 0.9021
- F1: 0.8844
- Accuracy: 0.9762

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2292        | 1.0   | 878  | 0.1048          | 0.8683    | 0.8973 | 0.8825 | 0.9763   |
| 0.0493        | 2.0   | 1756 | 0.1143          | 0.8674    | 0.9021 | 0.8844 | 0.9762   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
