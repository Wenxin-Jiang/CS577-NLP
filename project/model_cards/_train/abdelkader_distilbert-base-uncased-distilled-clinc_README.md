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
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9464516129032258
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3038
- Accuracy: 0.9465

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
| No log        | 1.0   | 318  | 2.8460          | 0.7506   |
| 3.322         | 2.0   | 636  | 1.4301          | 0.8532   |
| 3.322         | 3.0   | 954  | 0.7377          | 0.9152   |
| 1.2296        | 4.0   | 1272 | 0.4784          | 0.9316   |
| 0.449         | 5.0   | 1590 | 0.3730          | 0.9390   |
| 0.449         | 6.0   | 1908 | 0.3367          | 0.9429   |
| 0.2424        | 7.0   | 2226 | 0.3163          | 0.9468   |
| 0.1741        | 8.0   | 2544 | 0.3074          | 0.9452   |
| 0.1741        | 9.0   | 2862 | 0.3054          | 0.9458   |
| 0.1501        | 10.0  | 3180 | 0.3038          | 0.9465   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
