---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: dataset_model2
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
      value: 0.8797595190380761
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dataset_model2

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5350
- Accuracy: 0.8798

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1141        | 0.99  | 62   | 0.4707          | 0.8647   |
| 0.1098        | 1.99  | 124  | 0.4876          | 0.8597   |
| 0.1444        | 2.99  | 186  | 0.4651          | 0.8647   |
| 0.1088        | 3.99  | 248  | 0.5397          | 0.8527   |
| 0.1404        | 4.99  | 310  | 0.4794          | 0.8727   |
| 0.0656        | 5.99  | 372  | 0.5637          | 0.8507   |
| 0.1126        | 6.99  | 434  | 0.5318          | 0.8597   |
| 0.099         | 7.99  | 496  | 0.5522          | 0.8597   |
| 0.0501        | 8.99  | 558  | 0.5654          | 0.8667   |
| 0.0878        | 9.99  | 620  | 0.5915          | 0.8517   |
| 0.0594        | 10.99 | 682  | 0.5846          | 0.8717   |
| 0.0562        | 11.99 | 744  | 0.5191          | 0.8778   |
| 0.0554        | 12.99 | 806  | 0.5425          | 0.8717   |
| 0.0368        | 13.99 | 868  | 0.5725          | 0.8778   |
| 0.0415        | 14.99 | 930  | 0.5790          | 0.8637   |
| 0.0208        | 15.99 | 992  | 0.5319          | 0.8788   |
| 0.026         | 16.99 | 1054 | 0.5622          | 0.8677   |
| 0.0307        | 17.99 | 1116 | 0.5129          | 0.8878   |
| 0.015         | 18.99 | 1178 | 0.5508          | 0.8768   |
| 0.0263        | 19.99 | 1240 | 0.5350          | 0.8798   |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
