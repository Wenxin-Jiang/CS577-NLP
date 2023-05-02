---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v6_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v6_wikigold_split
      type: article250v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.3970455230630087
    - name: Recall
      type: recall
      value: 0.3699438202247191
    - name: F1
      type: f1
      value: 0.3830158499345645
    - name: Accuracy
      type: accuracy
      value: 0.8862729247713839
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v6_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3052
- Precision: 0.3970
- Recall: 0.3699
- F1: 0.3830
- Accuracy: 0.8863

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
| No log        | 1.0   | 29   | 0.5222          | 0.1785    | 0.0817 | 0.1121 | 0.8202   |
| No log        | 2.0   | 58   | 0.3356          | 0.3575    | 0.3357 | 0.3462 | 0.8780   |
| No log        | 3.0   | 87   | 0.3052          | 0.3970    | 0.3699 | 0.3830 | 0.8863   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
