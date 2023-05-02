---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- amazon_us_reviews
metrics:
- accuracy
model-index:
- name: test_trainer
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: amazon_us_reviews
      type: amazon_us_reviews
      config: Books_v1_01
      split: train[:1%]
      args: Books_v1_01
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7441424554826617
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test_trainer

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the amazon_us_reviews dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9348
- Accuracy: 0.7441

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.6471        | 1.0   | 7500  | 0.6596          | 0.7376   |
| 0.5235        | 2.0   | 15000 | 0.6997          | 0.7423   |
| 0.3955        | 3.0   | 22500 | 0.9348          | 0.7441   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
