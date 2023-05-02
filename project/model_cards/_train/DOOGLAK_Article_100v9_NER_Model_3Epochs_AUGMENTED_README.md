---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article100v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_100v9_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article100v9_wikigold_split
      type: article100v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.4912658530748983
    - name: Recall
      type: recall
      value: 0.5292601185872647
    - name: F1
      type: f1
      value: 0.5095557210225862
    - name: Accuracy
      type: accuracy
      value: 0.8976775418528724
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_100v9_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article100v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3011
- Precision: 0.4913
- Recall: 0.5293
- F1: 0.5096
- Accuracy: 0.8977

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
| No log        | 1.0   | 44   | 0.3780          | 0.3029    | 0.2939 | 0.2984 | 0.8623   |
| No log        | 2.0   | 88   | 0.3133          | 0.4705    | 0.4818 | 0.4761 | 0.8922   |
| No log        | 3.0   | 132  | 0.3011          | 0.4913    | 0.5293 | 0.5096 | 0.8977   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
