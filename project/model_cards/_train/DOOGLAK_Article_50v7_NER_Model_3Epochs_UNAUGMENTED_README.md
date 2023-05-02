---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article50v7_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_50v7_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article50v7_wikigold_split
      type: article50v7_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.3333333333333333
    - name: Recall
      type: recall
      value: 0.00024324981756263683
    - name: F1
      type: f1
      value: 0.0004861448711716091
    - name: Accuracy
      type: accuracy
      value: 0.7783221476510067
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_50v7_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article50v7_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7894
- Precision: 0.3333
- Recall: 0.0002
- F1: 0.0005
- Accuracy: 0.7783

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
| No log        | 1.0   | 6    | 1.0271          | 0.1183    | 0.0102 | 0.0188 | 0.7768   |
| No log        | 2.0   | 12   | 0.8250          | 0.4       | 0.0005 | 0.0010 | 0.7783   |
| No log        | 3.0   | 18   | 0.7894          | 0.3333    | 0.0002 | 0.0005 | 0.7783   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6