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
      value: 0.9454838709677419
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3120
- Accuracy: 0.9455

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
- num_epochs: 9

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 318  | 1.8803          | 0.7426   |
| 2.2488        | 2.0   | 636  | 0.9662          | 0.8626   |
| 2.2488        | 3.0   | 954  | 0.5640          | 0.9103   |
| 0.8679        | 4.0   | 1272 | 0.4093          | 0.9332   |
| 0.4101        | 5.0   | 1590 | 0.3554          | 0.9435   |
| 0.4101        | 6.0   | 1908 | 0.3312          | 0.9445   |
| 0.2894        | 7.0   | 2226 | 0.3179          | 0.9452   |
| 0.2496        | 8.0   | 2544 | 0.3137          | 0.9448   |
| 0.2496        | 9.0   | 2862 | 0.3120          | 0.9455   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
