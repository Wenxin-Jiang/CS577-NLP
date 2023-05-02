---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- image_folder
metrics:
- accuracy
model-index:
- name: violation-classification-bantai-vit-v80ep
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
      value: 0.9559725730783111
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# violation-classification-bantai-vit-v80ep

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the image_folder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1974
- Accuracy: 0.9560

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
- num_epochs: 80

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.797         | 4.95  | 500  | 0.3926          | 0.8715   |
| 0.3095        | 9.9   | 1000 | 0.2597          | 0.9107   |
| 0.1726        | 14.85 | 1500 | 0.2157          | 0.9253   |
| 0.1259        | 19.8  | 2000 | 0.1870          | 0.9392   |
| 0.0959        | 24.75 | 2500 | 0.1797          | 0.9444   |
| 0.0835        | 29.7  | 3000 | 0.2293          | 0.9354   |
| 0.0722        | 34.65 | 3500 | 0.1921          | 0.9441   |
| 0.0628        | 39.6  | 4000 | 0.1897          | 0.9491   |
| 0.059         | 44.55 | 4500 | 0.1719          | 0.9520   |
| 0.0531        | 49.5  | 5000 | 0.1987          | 0.9513   |
| 0.046         | 54.45 | 5500 | 0.1713          | 0.9556   |
| 0.0444        | 59.4  | 6000 | 0.2016          | 0.9525   |
| 0.042         | 64.36 | 6500 | 0.1950          | 0.9525   |
| 0.0363        | 69.31 | 7000 | 0.2017          | 0.9549   |
| 0.037         | 74.26 | 7500 | 0.1943          | 0.9551   |
| 0.0343        | 79.21 | 8000 | 0.1974          | 0.9560   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
