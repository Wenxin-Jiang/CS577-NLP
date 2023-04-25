---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: distilbert-base-uncased-finetuned-cola
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.51728018358102
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8815
- Matthews Correlation: 0.5173

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

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.5272        | 1.0   | 535  | 0.5099          | 0.4093               |
| 0.3563        | 2.0   | 1070 | 0.5114          | 0.5019               |
| 0.2425        | 3.0   | 1605 | 0.6696          | 0.4898               |
| 0.1726        | 4.0   | 2140 | 0.7715          | 0.5123               |
| 0.132         | 5.0   | 2675 | 0.8815          | 0.5173               |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.1
- Datasets 1.14.0
- Tokenizers 0.10.3
