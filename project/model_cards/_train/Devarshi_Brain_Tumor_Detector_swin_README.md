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
- name: Brain_Tumor_Detector_swin
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
      value: 0.9981308411214953
    - name: F1
      type: f1
      value: 0.9985111662531018
    - name: Recall
      type: recall
      value: 0.9990069513406157
    - name: Precision
      type: precision
      value: 0.998015873015873
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Brain_Tumor_Detector_swin

This model is a fine-tuned version of [microsoft/swin-base-patch4-window7-224-in22k](https://huggingface.co/microsoft/swin-base-patch4-window7-224-in22k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0054
- Accuracy: 0.9981
- F1: 0.9985
- Recall: 0.9990
- Precision: 0.9980

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
| 0.079         | 1.0   | 113  | 0.0283          | 0.9882   | 0.9906 | 0.9930 | 0.9881    |
| 0.0575        | 2.0   | 226  | 0.0121          | 0.9956   | 0.9965 | 0.9950 | 0.9980    |
| 0.0312        | 3.0   | 339  | 0.0054          | 0.9981   | 0.9985 | 0.9990 | 0.9980    |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.1
