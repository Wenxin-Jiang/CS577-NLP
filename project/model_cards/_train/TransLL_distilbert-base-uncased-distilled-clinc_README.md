---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-distilled-clinc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: clinc_oos
      type: clinc_oos
      config: plus
      split: train
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9503225806451613
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3186
- Accuracy: 0.9503

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
- train_batch_size: 48
- eval_batch_size: 48
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 318  | 2.0524          | 0.7519   |
| 2.4405        | 2.0   | 636  | 1.0364          | 0.8623   |
| 2.4405        | 3.0   | 954  | 0.5867          | 0.9187   |
| 0.921         | 4.0   | 1272 | 0.4271          | 0.9361   |
| 0.417         | 5.0   | 1590 | 0.3687          | 0.9442   |
| 0.417         | 6.0   | 1908 | 0.3438          | 0.9484   |
| 0.2885        | 7.0   | 2226 | 0.3292          | 0.95     |
| 0.2454        | 8.0   | 2544 | 0.3235          | 0.9490   |
| 0.2454        | 9.0   | 2862 | 0.3206          | 0.95     |
| 0.2309        | 10.0  | 3180 | 0.3186          | 0.9503   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
