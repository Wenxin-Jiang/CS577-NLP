---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: movieHunt4-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# movieHunt4-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0005
- Precision: 1.0
- Recall: 1.0
- F1: 1.0
- Accuracy: 1.0

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 48   | 0.0284          | 0.9959    | 0.9959 | 0.9959 | 0.9974   |
| No log        | 2.0   | 96   | 0.0060          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 3.0   | 144  | 0.0034          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 4.0   | 192  | 0.0025          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 5.0   | 240  | 0.0020          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 6.0   | 288  | 0.0016          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 7.0   | 336  | 0.0014          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 8.0   | 384  | 0.0012          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 9.0   | 432  | 0.0011          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 10.0  | 480  | 0.0010          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 11.0  | 528  | 0.0009          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 12.0  | 576  | 0.0009          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 13.0  | 624  | 0.0008          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 14.0  | 672  | 0.0008          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 15.0  | 720  | 0.0008          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 16.0  | 768  | 0.0007          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 17.0  | 816  | 0.0007          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 18.0  | 864  | 0.0007          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 19.0  | 912  | 0.0006          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0168        | 20.0  | 960  | 0.0006          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 21.0  | 1008 | 0.0006          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 22.0  | 1056 | 0.0006          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 23.0  | 1104 | 0.0006          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 24.0  | 1152 | 0.0006          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 25.0  | 1200 | 0.0005          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 26.0  | 1248 | 0.0005          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 27.0  | 1296 | 0.0005          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 28.0  | 1344 | 0.0005          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 29.0  | 1392 | 0.0005          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0014        | 30.0  | 1440 | 0.0005          | 1.0       | 1.0    | 1.0    | 1.0      |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
