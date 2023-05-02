---
tags:
- generated_from_trainer
datasets:
- ncbi_disease
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biobert-finetuned-ncbi
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: ncbi_disease
      type: ncbi_disease
      config: ncbi_disease
      split: train
      args: ncbi_disease
    metrics:
    - name: Precision
      type: precision
      value: 0.8192771084337349
    - name: Recall
      type: recall
      value: 0.8640406607369758
    - name: F1
      type: f1
      value: 0.8410636982065552
    - name: Accuracy
      type: accuracy
      value: 0.9856218100336114
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-finetuned-ncbi

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on the ncbi_disease dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0590
- Precision: 0.8193
- Recall: 0.8640
- F1: 0.8411
- Accuracy: 0.9856

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1049        | 1.0   | 680  | 0.0588          | 0.7826    | 0.7776 | 0.7801 | 0.9806   |
| 0.0362        | 2.0   | 1360 | 0.0539          | 0.8084    | 0.8577 | 0.8323 | 0.9852   |
| 0.0109        | 3.0   | 2040 | 0.0590          | 0.8193    | 0.8640 | 0.8411 | 0.9856   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
