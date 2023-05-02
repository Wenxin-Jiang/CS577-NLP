---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- yelp_review_full
metrics:
- accuracy
model-index:
- name: 22s-dl-sentiment-1
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: yelp_review_full
      type: yelp_review_full
      args: yelp_review_full
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9542333333333334
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 22s-dl-sentiment-1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the yelp_review_full dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2574
- Accuracy: 0.9542

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



### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.3.0
- Tokenizers 0.12.1
