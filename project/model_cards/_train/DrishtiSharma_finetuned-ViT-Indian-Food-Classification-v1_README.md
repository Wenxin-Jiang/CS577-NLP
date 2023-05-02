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
- name: finetuned-ViT-Indian-Food-Classification-v1
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: Human_Action_Recognition
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9341126461211477
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-ViT-Indian-Food-Classification-v1

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the Human_Action_Recognition dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2665
- Accuracy: 0.9341

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
| 1.2019        | 0.3   | 100  | 0.9317          | 0.8555   |
| 0.6664        | 0.6   | 200  | 0.5432          | 0.8959   |
| 0.5096        | 0.9   | 300  | 0.4700          | 0.8990   |
| 0.6116        | 1.2   | 400  | 0.4504          | 0.8799   |
| 0.4326        | 1.5   | 500  | 0.3856          | 0.8980   |
| 0.3349        | 1.8   | 600  | 0.3471          | 0.9129   |
| 0.5141        | 2.1   | 700  | 0.3708          | 0.9033   |
| 0.32          | 2.4   | 800  | 0.3338          | 0.9139   |
| 0.2611        | 2.7   | 900  | 0.3159          | 0.9171   |
| 0.1836        | 3.0   | 1000 | 0.2696          | 0.9299   |
| 0.2492        | 3.3   | 1100 | 0.2979          | 0.9214   |
| 0.1846        | 3.6   | 1200 | 0.3165          | 0.9203   |
| 0.1505        | 3.9   | 1300 | 0.2806          | 0.9288   |
| 0.1854        | 4.2   | 1400 | 0.2665          | 0.9341   |
| 0.124         | 4.5   | 1500 | 0.2695          | 0.9341   |
| 0.0719        | 4.8   | 1600 | 0.2668          | 0.9320   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
