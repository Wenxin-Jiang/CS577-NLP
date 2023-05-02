---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- yelp_review_full
metrics:
- accuracy
model-index:
- name: Bert_Classifier
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
      value: 0.5133333333333333
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bert_Classifier

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the yelp_review_full dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8684
- Accuracy: 0.5133

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 188  | 2.3115          | 0.5267   |
| No log        | 2.0   | 376  | 2.5268          | 0.5467   |
| 0.2313        | 3.0   | 564  | 2.8684          | 0.5133   |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
