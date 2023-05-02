---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v2_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v2_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v2_wikigold_split
      type: article250v2_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6846043165467626
    - name: Recall
      type: recall
      value: 0.680881511161992
    - name: F1
      type: f1
      value: 0.6827378390012915
    - name: Accuracy
      type: accuracy
      value: 0.928421690702902
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v2_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v2_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2484
- Precision: 0.6846
- Recall: 0.6809
- F1: 0.6827
- Accuracy: 0.9284

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
| No log        | 1.0   | 102  | 0.2354          | 0.6141    | 0.6162 | 0.6151 | 0.9221   |
| No log        | 2.0   | 204  | 0.2347          | 0.6732    | 0.6840 | 0.6786 | 0.9290   |
| No log        | 3.0   | 306  | 0.2484          | 0.6846    | 0.6809 | 0.6827 | 0.9284   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
