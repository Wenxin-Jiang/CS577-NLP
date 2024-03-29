---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article50v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_50v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article50v4_wikigold_split
      type: article50v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.24415926291543272
    - name: Recall
      type: recall
      value: 0.180359747204667
    - name: F1
      type: f1
      value: 0.20746539913323078
    - name: Accuracy
      type: accuracy
      value: 0.8391882216056565
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_50v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article50v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4148
- Precision: 0.2442
- Recall: 0.1804
- F1: 0.2075
- Accuracy: 0.8392

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
| No log        | 1.0   | 26   | 0.5371          | 0.2683    | 0.0632 | 0.1023 | 0.7953   |
| No log        | 2.0   | 52   | 0.4314          | 0.2259    | 0.1575 | 0.1856 | 0.8325   |
| No log        | 3.0   | 78   | 0.4148          | 0.2442    | 0.1804 | 0.2075 | 0.8392   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
