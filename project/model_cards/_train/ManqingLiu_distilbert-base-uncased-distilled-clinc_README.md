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
      value: 0.9390322580645162
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0990
- Accuracy: 0.9390

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
| 1.0901        | 1.0   | 318  | 0.6293          | 0.7026   |
| 0.4796        | 2.0   | 636  | 0.2666          | 0.8661   |
| 0.2386        | 3.0   | 954  | 0.1553          | 0.9148   |
| 0.1591        | 4.0   | 1272 | 0.1238          | 0.9271   |
| 0.1309        | 5.0   | 1590 | 0.1121          | 0.9339   |
| 0.118         | 6.0   | 1908 | 0.1065          | 0.9371   |
| 0.11          | 7.0   | 2226 | 0.1033          | 0.9394   |
| 0.1057        | 8.0   | 2544 | 0.1002          | 0.9377   |
| 0.1032        | 9.0   | 2862 | 0.0995          | 0.9384   |
| 0.1014        | 10.0  | 3180 | 0.0990          | 0.9390   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.12.0+cu113
- Datasets 1.16.1
- Tokenizers 0.10.3
