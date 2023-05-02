---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v9_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v9_wikigold_split
      type: article250v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6808931599773883
    - name: Recall
      type: recall
      value: 0.6954387990762124
    - name: F1
      type: f1
      value: 0.68808911739503
    - name: Accuracy
      type: accuracy
      value: 0.9338001436339386
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v9_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2025
- Precision: 0.6809
- Recall: 0.6954
- F1: 0.6881
- Accuracy: 0.9338

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
| No log        | 1.0   | 98   | 0.2169          | 0.5997    | 0.6579 | 0.6275 | 0.9256   |
| No log        | 2.0   | 196  | 0.2077          | 0.6791    | 0.6804 | 0.6797 | 0.9317   |
| No log        | 3.0   | 294  | 0.2025          | 0.6809    | 0.6954 | 0.6881 | 0.9338   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
