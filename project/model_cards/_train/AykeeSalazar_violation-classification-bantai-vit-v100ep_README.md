---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- image_folder
metrics:
- accuracy
model-index:
- name: violation-classification-bantai-vit-v100ep
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: image_folder
      type: image_folder
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9157343919162757
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# violation-classification-bantai-vit-v100ep

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the image_folder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2557
- Accuracy: 0.9157

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 100

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2811        | 1.0   | 101  | 0.2855          | 0.9027   |
| 0.2382        | 2.0   | 202  | 0.2763          | 0.9085   |
| 0.2361        | 3.0   | 303  | 0.2605          | 0.9109   |
| 0.196         | 4.0   | 404  | 0.2652          | 0.9110   |
| 0.1395        | 5.0   | 505  | 0.2648          | 0.9134   |
| 0.155         | 6.0   | 606  | 0.2656          | 0.9152   |
| 0.1422        | 7.0   | 707  | 0.2607          | 0.9141   |
| 0.1511        | 8.0   | 808  | 0.2557          | 0.9157   |
| 0.1938        | 9.0   | 909  | 0.2679          | 0.9049   |
| 0.2094        | 10.0  | 1010 | 0.2392          | 0.9137   |
| 0.1835        | 11.0  | 1111 | 0.2400          | 0.9156   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
