---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- dfl
metrics:
- f1
model-index:
- name: vit_for_dfl
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: dfl
      type: dfl
      config: small
      split: train
      args: small
    metrics:
    - name: F1
      type: f1
      value: 0.2452846975088968
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit_for_dfl

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the dfl dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1771
- F1: 0.2453

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0836        | 1.0   | 358  | 0.1841          | 0.2453 |
| 0.207         | 2.0   | 716  | 0.1835          | 0.2453 |
| 0.2325        | 3.0   | 1074 | 0.1771          | 0.2453 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
