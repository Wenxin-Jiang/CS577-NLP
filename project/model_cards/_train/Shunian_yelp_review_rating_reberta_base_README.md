---
tags:
- generated_from_trainer
datasets:
- yelp_review_full
metrics:
- accuracy
model-index:
- name: yelp_review_rating_reberta_base
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
      value: 0.67086
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# yelp_review_rating_reberta_base

This model was trained from scratch on the yelp_review_full dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8071
- Accuracy: 0.6709

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
- lr_scheduler_type: cosine
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step   | Accuracy | Validation Loss |
|:-------------:|:-----:|:------:|:--------:|:---------------:|
| 0.8355        | 1.0   | 40625  | 0.6449   | 0.8211          |
| 0.7709        | 2.0   | 81250  | 0.6615   | 0.7877          |
| 0.7141        | 3.0   | 121875 | 0.6712   | 0.7689          |
| 0.6511        | 4.0   | 162500 | 0.6724   | 0.7845          |
| 0.6229        | 5.0   | 203125 | 0.6719   | 0.8009          |
| 0.6036        | 6.0   | 243750 | 0.8071   | 0.6709          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu102
- Datasets 2.6.1
- Tokenizers 0.12.1
