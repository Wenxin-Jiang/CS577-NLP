---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: bert-base-cased-cola
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE COLA
      type: glue
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.5794528111058918
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-cola

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the GLUE COLA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3976
- Matthews Correlation: 0.5795

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.5733        | 0.93  | 500  | 0.4877          | 0.5001               |
| 0.3426        | 1.87  | 1000 | 0.3976          | 0.5795               |
| 0.2321        | 2.8   | 1500 | 0.6284          | 0.6034               |
| 0.1599        | 3.74  | 2000 | 0.6997          | 0.5718               |
| 0.123         | 4.67  | 2500 | 0.8962          | 0.5624               |
| 0.0888        | 5.61  | 3000 | 0.8743          | 0.5857               |
| 0.0659        | 6.54  | 3500 | 0.9159          | 0.5962               |
| 0.0385        | 7.48  | 4000 | 1.2283          | 0.5704               |
| 0.0299        | 8.41  | 4500 | 1.2601          | 0.5662               |
| 0.0211        | 9.35  | 5000 | 1.2885          | 0.5629               |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.7.1
- Datasets 1.18.3
- Tokenizers 0.11.6
