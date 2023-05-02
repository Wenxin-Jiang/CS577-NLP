---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vit-base-patch16-224-in21k_Simpsons_Family_Members
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
      value: 0.9529702970297029
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_Simpsons_Family_Members

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2431
- Accuracy: 0.9530
- Weighted f1: 0.9522
- Micro f1: 0.9530
- Macro f1: 0.9521
- Weighted recall: 0.9530
- Micro recall: 0.9530
- Macro recall: 0.9531
- Weighted precision: 0.9605
- Micro precision: 0.9530
- Macro precision: 0.9601

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Weighted f1 | Micro f1 | Macro f1 | Weighted recall | Micro recall | Macro recall | Weighted precision | Micro precision | Macro precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----------:|:--------:|:--------:|:---------------:|:------------:|:------------:|:------------------:|:---------------:|:---------------:|
| 1.5773        | 1.0   | 373  | 1.0482          | 0.7772   | 0.7263      | 0.7772   | 0.7261   | 0.7772          | 0.7772       | 0.7778       | 0.8933             | 0.7772          | 0.8922          |
| 0.1598        | 2.0   | 746  | 0.3902          | 0.9059   | 0.9028      | 0.9059   | 0.9026   | 0.9059          | 0.9059       | 0.9060       | 0.9224             | 0.9059          | 0.9219          |
| 0.027         | 3.0   | 1119 | 0.2431          | 0.9530   | 0.9522      | 0.9530   | 0.9521   | 0.9530          | 0.9530       | 0.9531       | 0.9605             | 0.9530          | 0.9601          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
