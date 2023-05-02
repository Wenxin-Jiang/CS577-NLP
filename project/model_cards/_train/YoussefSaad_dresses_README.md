---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: dresses
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
      value: 0.9013840830449827
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dresses

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4588
- Accuracy: 0.9014

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
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2458        | 1.23  | 100  | 0.4519          | 0.8633   |
| 0.0937        | 2.47  | 200  | 0.4285          | 0.8754   |
| 0.0802        | 3.7   | 300  | 0.4683          | 0.8754   |
| 0.041         | 4.94  | 400  | 0.4088          | 0.9031   |
| 0.0277        | 6.17  | 500  | 0.3979          | 0.8945   |
| 0.0459        | 7.41  | 600  | 0.4253          | 0.9014   |
| 0.024         | 8.64  | 700  | 0.4680          | 0.8893   |
| 0.0267        | 9.88  | 800  | 0.4575          | 0.8945   |
| 0.019         | 11.11 | 900  | 0.4470          | 0.8893   |
| 0.0235        | 12.35 | 1000 | 0.4380          | 0.9066   |
| 0.0129        | 13.58 | 1100 | 0.4557          | 0.9048   |
| 0.0211        | 14.81 | 1200 | 0.4588          | 0.9014   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
