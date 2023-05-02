---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- amazon_reviews_multi
metrics:
- accuracy
model-index:
- name: results
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
      value: 0.8404
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on the amazon_reviews_multi dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3793
- Accuracy: 0.8404

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.3542        | 1.0   | 125  | 0.3611          | 0.839    |
| 0.2255        | 2.0   | 250  | 0.3793          | 0.8404   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.12.1
- Tokenizers 0.10.3
