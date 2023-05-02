---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: bags_results
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 1.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bags_results

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0002
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
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0485        | 0.23  | 100  | 0.0119          | 0.9974   |
| 0.0029        | 0.45  | 200  | 0.0105          | 0.9983   |
| 0.0029        | 0.68  | 300  | 0.0080          | 0.9974   |
| 0.0331        | 0.91  | 400  | 0.0014          | 1.0      |
| 0.0019        | 1.13  | 500  | 0.0105          | 0.9974   |
| 0.0008        | 1.36  | 600  | 0.0058          | 0.9991   |
| 0.0083        | 1.59  | 700  | 0.0133          | 0.9957   |
| 0.0009        | 1.81  | 800  | 0.0028          | 0.9991   |
| 0.0005        | 2.04  | 900  | 0.0030          | 0.9991   |
| 0.0005        | 2.27  | 1000 | 0.0016          | 0.9991   |
| 0.0024        | 2.49  | 1100 | 0.0004          | 1.0      |
| 0.0003        | 2.72  | 1200 | 0.0004          | 1.0      |
| 0.0003        | 2.95  | 1300 | 0.0016          | 0.9991   |
| 0.0003        | 3.17  | 1400 | 0.0009          | 0.9991   |
| 0.0003        | 3.4   | 1500 | 0.0003          | 1.0      |
| 0.0002        | 3.63  | 1600 | 0.0002          | 1.0      |
| 0.0002        | 3.85  | 1700 | 0.0002          | 1.0      |
| 0.0002        | 4.08  | 1800 | 0.0002          | 1.0      |
| 0.0002        | 4.31  | 1900 | 0.0002          | 1.0      |
| 0.0002        | 4.54  | 2000 | 0.0002          | 1.0      |
| 0.0002        | 4.76  | 2100 | 0.0002          | 1.0      |
| 0.0002        | 4.99  | 2200 | 0.0002          | 1.0      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
