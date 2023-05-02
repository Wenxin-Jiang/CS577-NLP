---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- yelp_review_full
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned-yelp-reviews
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
      value: 0.6418461538461538
    - name: F1
      type: f1
      value: 0.6424942003355615
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-yelp-reviews

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the yelp_review_full dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8288
- Accuracy: 0.6418
- F1: 0.6425

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.8991        | 1.0   | 1524 | 0.8396          | 0.6302   | 0.6294 |
| 0.754         | 2.0   | 3048 | 0.8288          | 0.6418   | 0.6425 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
