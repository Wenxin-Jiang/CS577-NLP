---
tags:
- generated_from_trainer
datasets:
- yelp_review_full
metrics:
- accuracy
model-index:
- name: yelp_review_classification
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: yelp_review_full
      type: yelp_review_full
      config: yelp_review_full
      split: train
      args: yelp_review_full
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6852
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# yelp_review_classification

This model was trained from scratch on the yelp_review_full dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8517
- Accuracy: 0.6852

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step   | Accuracy | Validation Loss |
|:-------------:|:-----:|:------:|:--------:|:---------------:|
| 0.7149        | 1.0   | 40625  | 0.6889   | 0.7167          |
| 0.6501        | 2.0   | 81250  | 0.6967   | 0.6979          |
| 0.5547        | 3.0   | 121875 | 0.6915   | 0.7377          |
| 0.5375        | 4.0   | 162500 | 0.6895   | 0.7611          |
| 0.4386        | 5.0   | 203125 | 0.8517   | 0.6852          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu102
- Datasets 2.5.2
- Tokenizers 0.12.1
