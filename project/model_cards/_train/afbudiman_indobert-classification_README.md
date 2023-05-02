---
license: mit
tags:
- generated_from_trainer
datasets:
- indonlu
metrics:
- accuracy
- f1
model-index:
- name: indobert-classification
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: indonlu
      type: indonlu
      args: smsa
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9396825396825397
    - name: F1
      type: f1
      value: 0.9393057427148881
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indobert-classification

This model is a fine-tuned version of [indobenchmark/indobert-base-p1](https://huggingface.co/indobenchmark/indobert-base-p1) on the indonlu dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3707
- Accuracy: 0.9397
- F1: 0.9393

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.2458        | 1.0   | 688  | 0.2229          | 0.9325   | 0.9323 |
| 0.1258        | 2.0   | 1376 | 0.2332          | 0.9373   | 0.9369 |
| 0.059         | 3.0   | 2064 | 0.3389          | 0.9365   | 0.9365 |
| 0.0268        | 4.0   | 2752 | 0.3412          | 0.9421   | 0.9417 |
| 0.0097        | 5.0   | 3440 | 0.3707          | 0.9397   | 0.9393 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
