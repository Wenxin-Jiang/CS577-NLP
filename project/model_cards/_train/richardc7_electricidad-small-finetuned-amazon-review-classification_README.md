---
tags:
- generated_from_trainer
datasets:
- amazon_reviews_multi
metrics:
- accuracy
model-index:
- name: electricidad-small-finetuned-amazon-review-classification
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: amazon_reviews_multi
      type: amazon_reviews_multi
      args: es
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.581
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# electricidad-small-finetuned-amazon-review-classification

This model is a fine-tuned version of [mrm8488/electricidad-small-discriminator](https://huggingface.co/mrm8488/electricidad-small-discriminator) on the amazon_reviews_multi dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9601
- Accuracy: 0.581

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 1.0136        | 1.0   | 25000 | 1.0153          | 0.5414   |
| 0.9416        | 2.0   | 50000 | 0.9942          | 0.5576   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
