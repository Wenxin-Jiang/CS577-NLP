---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
- f1
- recall
- precision
model-index:
- name: Brain_Tumor_Class_swin
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
      value: 0.9936204146730463
    - name: F1
      type: f1
      value: 0.9936204146730463
    - name: Recall
      type: recall
      value: 0.9936204146730463
    - name: Precision
      type: precision
      value: 0.9936204146730463
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Brain_Tumor_Class_swin

This model is a fine-tuned version of [microsoft/swin-base-patch4-window7-224-in22k](https://huggingface.co/microsoft/swin-base-patch4-window7-224-in22k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0220
- Accuracy: 0.9936
- F1: 0.9936
- Recall: 0.9936
- Precision: 0.9936

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.1248        | 1.0   | 220  | 0.0610          | 0.9767   | 0.9767 | 0.9767 | 0.9767    |
| 0.0887        | 2.0   | 440  | 0.0300          | 0.9920   | 0.9920 | 0.9920 | 0.9920    |
| 0.0449        | 3.0   | 660  | 0.0220          | 0.9936   | 0.9936 | 0.9936 | 0.9936    |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.1
