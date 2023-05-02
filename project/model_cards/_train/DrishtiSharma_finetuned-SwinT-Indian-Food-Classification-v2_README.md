---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: finetuned-SwinT-Indian-Food-Classification-v2
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: Indian-Food-Images
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9458023379383634
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-SwinT-Indian-Food-Classification-v2

This model is a fine-tuned version of [microsoft/swin-base-patch4-window7-224-in22k](https://huggingface.co/microsoft/swin-base-patch4-window7-224-in22k) on the Indian-Food-Images dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2226
- Accuracy: 0.9458

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
| 0.9351        | 0.3   | 100  | 0.6017          | 0.8363   |
| 0.5667        | 0.6   | 200  | 0.4384          | 0.8767   |
| 0.5548        | 0.9   | 300  | 0.4215          | 0.8767   |
| 0.5516        | 1.2   | 400  | 0.4290          | 0.8735   |
| 0.3782        | 1.5   | 500  | 0.3502          | 0.8980   |
| 0.3115        | 1.8   | 600  | 0.3780          | 0.8937   |
| 0.4229        | 2.1   | 700  | 0.3545          | 0.8905   |
| 0.3832        | 2.4   | 800  | 0.3446          | 0.9086   |
| 0.2745        | 2.7   | 900  | 0.3299          | 0.9150   |
| 0.2063        | 3.0   | 1000 | 0.2592          | 0.9277   |
| 0.2077        | 3.3   | 1100 | 0.3772          | 0.9150   |
| 0.2041        | 3.6   | 1200 | 0.2855          | 0.9214   |
| 0.2541        | 3.9   | 1300 | 0.2502          | 0.9330   |
| 0.1203        | 4.2   | 1400 | 0.2577          | 0.9362   |
| 0.1594        | 4.5   | 1500 | 0.2226          | 0.9458   |
| 0.1015        | 4.8   | 1600 | 0.2368          | 0.9437   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
