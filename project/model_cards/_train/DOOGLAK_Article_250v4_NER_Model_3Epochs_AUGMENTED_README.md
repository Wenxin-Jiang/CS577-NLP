---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v4_wikigold_split
      type: article250v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.630065717415115
    - name: Recall
      type: recall
      value: 0.638457269700333
    - name: F1
      type: f1
      value: 0.6342337375964718
    - name: Accuracy
      type: accuracy
      value: 0.9238909136609275
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2337
- Precision: 0.6301
- Recall: 0.6385
- F1: 0.6342
- Accuracy: 0.9239

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
| No log        | 1.0   | 96   | 0.2343          | 0.5944    | 0.6046 | 0.5994 | 0.9191   |
| No log        | 2.0   | 192  | 0.2215          | 0.6239    | 0.6412 | 0.6325 | 0.9251   |
| No log        | 3.0   | 288  | 0.2337          | 0.6301    | 0.6385 | 0.6342 | 0.9239   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
