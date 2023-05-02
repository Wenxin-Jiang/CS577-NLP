---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v3_wikigold_split
      type: article250v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6347305389221557
    - name: Recall
      type: recall
      value: 0.6341880341880342
    - name: F1
      type: f1
      value: 0.6344591705857204
    - name: Accuracy
      type: accuracy
      value: 0.920652258718889
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2531
- Precision: 0.6347
- Recall: 0.6342
- F1: 0.6345
- Accuracy: 0.9207

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
| No log        | 1.0   | 82   | 0.2668          | 0.5478    | 0.5370 | 0.5424 | 0.9064   |
| No log        | 2.0   | 164  | 0.2516          | 0.6272    | 0.6154 | 0.6212 | 0.9179   |
| No log        | 3.0   | 246  | 0.2531          | 0.6347    | 0.6342 | 0.6345 | 0.9207   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
