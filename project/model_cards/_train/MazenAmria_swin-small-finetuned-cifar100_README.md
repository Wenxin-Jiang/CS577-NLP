---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cifar100
metrics:
- accuracy
model-index:
- name: swin-small-finetuned-cifar100
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: cifar100
      type: cifar100
      args: cifar100
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8938
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-small-finetuned-cifar100

This model is a fine-tuned version of [microsoft/swin-small-patch4-window7-224](https://huggingface.co/microsoft/swin-small-patch4-window7-224) on the cifar100 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6281
- Accuracy: 0.8938

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.72          | 1.0   | 781   | 0.6691          | 0.8077   |
| 0.6944        | 2.0   | 1562  | 0.4797          | 0.8495   |
| 0.2794        | 3.0   | 2343  | 0.4338          | 0.869    |
| 0.2569        | 4.0   | 3124  | 0.4263          | 0.879    |
| 0.1417        | 5.0   | 3905  | 0.4385          | 0.8819   |
| 0.0961        | 6.0   | 4686  | 0.4720          | 0.8854   |
| 0.0584        | 7.0   | 5467  | 0.4941          | 0.885    |
| 0.0351        | 8.0   | 6248  | 0.5253          | 0.885    |
| 0.0107        | 9.0   | 7029  | 0.5598          | 0.8887   |
| 0.0118        | 10.0  | 7810  | 0.5998          | 0.8858   |
| 0.0097        | 11.0  | 8591  | 0.5957          | 0.8941   |
| 0.0044        | 12.0  | 9372  | 0.6237          | 0.8912   |
| 0.0013        | 13.0  | 10153 | 0.6286          | 0.8929   |
| 0.0102        | 14.0  | 10934 | 0.6281          | 0.8938   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
