---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
datasets:
- snacks
metrics:
- accuracy
model-index:
- name: vit-snacks
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: Matthijs/snacks
      type: snacks
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9392670157068063
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-snacks

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the Matthijs/snacks dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2754
- Accuracy: 0.9393

## Model description

upload any image of your fave yummy snack 

## Intended uses & limitations

there are only 20 different varieties of snacks

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

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.8724        | 0.33  | 100  | 0.9118          | 0.8670   |
| 0.5628        | 0.66  | 200  | 0.6873          | 0.8471   |
| 0.4421        | 0.99  | 300  | 0.4995          | 0.8691   |
| 0.2837        | 1.32  | 400  | 0.4008          | 0.9026   |
| 0.1645        | 1.65  | 500  | 0.3702          | 0.9058   |
| 0.1604        | 1.98  | 600  | 0.3981          | 0.8921   |
| 0.0498        | 2.31  | 700  | 0.3185          | 0.9204   |
| 0.0406        | 2.64  | 800  | 0.3427          | 0.9141   |
| 0.1049        | 2.97  | 900  | 0.3444          | 0.9173   |
| 0.0272        | 3.3   | 1000 | 0.3168          | 0.9246   |
| 0.0186        | 3.63  | 1100 | 0.3142          | 0.9288   |
| 0.0203        | 3.96  | 1200 | 0.2931          | 0.9298   |
| 0.007         | 4.29  | 1300 | 0.2754          | 0.9393   |
| 0.0072        | 4.62  | 1400 | 0.2778          | 0.9403   |
| 0.0073        | 4.95  | 1500 | 0.2782          | 0.9393   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
