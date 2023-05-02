---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- image_folder
metrics:
- accuracy
model-index:
- name: swin-tiny-patch4-window7-224-finetuned-eurosat
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
      value: 0.9393939393939394
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-tiny-patch4-window7-224-finetuned-eurosat

This model is a fine-tuned version of [microsoft/swin-tiny-patch4-window7-224](https://huggingface.co/microsoft/swin-tiny-patch4-window7-224) on the image_folder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1677
- Accuracy: 0.9394

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 7    | 0.3554          | 0.8081   |
| 0.4819        | 2.0   | 14   | 0.2077          | 0.9091   |
| 0.1985        | 3.0   | 21   | 0.1677          | 0.9394   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cpu
- Datasets 2.2.0
- Tokenizers 0.12.1
