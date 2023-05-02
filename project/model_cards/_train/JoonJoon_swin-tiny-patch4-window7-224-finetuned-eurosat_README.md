---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: swin-tiny-patch4-window7-224-finetuned-eurosat
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9725925925925926
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-tiny-patch4-window7-224-finetuned-eurosat

This model is a fine-tuned version of [microsoft/swin-tiny-patch4-window7-224](https://huggingface.co/microsoft/swin-tiny-patch4-window7-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0814
- Accuracy: 0.9726

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
- train_batch_size: 96
- eval_batch_size: 96
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 384
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.3216        | 0.99  | 63   | 0.1349          | 0.9589   |
| 0.2           | 1.99  | 126  | 0.0873          | 0.9704   |
| 0.1664        | 2.99  | 189  | 0.0814          | 0.9726   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2+cu102
- Datasets 2.3.2
- Tokenizers 0.11.6
