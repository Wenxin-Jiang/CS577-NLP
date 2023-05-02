---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v7_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v7_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v7_wikigold_split
      type: article250v7_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6857221006564551
    - name: Recall
      type: recall
      value: 0.7036205444849846
    - name: F1
      type: f1
      value: 0.6945560326915085
    - name: Accuracy
      type: accuracy
      value: 0.9325670690390745
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v7_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v7_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2210
- Precision: 0.6857
- Recall: 0.7036
- F1: 0.6946
- Accuracy: 0.9326

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
| No log        | 1.0   | 94   | 0.2230          | 0.6381    | 0.6587 | 0.6483 | 0.9244   |
| No log        | 2.0   | 188  | 0.2181          | 0.6882    | 0.6851 | 0.6866 | 0.9299   |
| No log        | 3.0   | 282  | 0.2210          | 0.6857    | 0.7036 | 0.6946 | 0.9326   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
