---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- inspec
metrics:
- f1
- precision
- recall
model-index:
- name: bert-finetuned-inspec-3-epochs
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: inspec
      type: inspec
      args: extraction
    metrics:
    - name: F1
      type: f1
      value: 0.28328008519701814
    - name: Precision
      type: precision
      value: 0.26594090202177295
    - name: Recall
      type: recall
      value: 0.3030379746835443
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-inspec-3-epochs

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the inspec dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2728
- F1: 0.2833
- Precision: 0.2659
- Recall: 0.3030

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
- seed: 0
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:------:|:---------:|:------:|
| 0.3338        | 1.0   | 125  | 0.2837          | 0.1401 | 0.1510    | 0.1306 |
| 0.2575        | 2.0   | 250  | 0.2658          | 0.2183 | 0.2519    | 0.1927 |
| 0.2259        | 3.0   | 375  | 0.2728          | 0.2833 | 0.2659    | 0.3030 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1
