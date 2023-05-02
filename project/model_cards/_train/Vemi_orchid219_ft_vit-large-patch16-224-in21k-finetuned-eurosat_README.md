---
tags:
- generated_from_trainer
datasets:
- image_folder
metrics:
- accuracy
model-index:
- name: orchid219_ft_vit-large-patch16-224-in21k-finetuned-eurosat
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
      value: 0.9230769230769231
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# orchid219_ft_vit-large-patch16-224-in21k-finetuned-eurosat

This model is a fine-tuned version of [gary109/orchid219_ft_vit-large-patch16-224-in21k](https://huggingface.co/gary109/orchid219_ft_vit-large-patch16-224-in21k) on the image_folder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9545
- Accuracy: 0.9231

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
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.5728        | 0.96  | 17   | 2.1936          | 0.8718   |
| 1.6005        | 1.96  | 34   | 1.2044          | 0.9359   |
| 0.9764        | 2.96  | 51   | 0.9545          | 0.9231   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
