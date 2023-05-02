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
- name: Brain_Tumor_Classification
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
      value: 0.9646761984861227
    - name: F1
      type: f1
      value: 0.9646761984861227
    - name: Recall
      type: recall
      value: 0.9646761984861227
    - name: Precision
      type: precision
      value: 0.9646761984861227
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Brain_Tumor_Classification

This model is a fine-tuned version of [microsoft/swin-tiny-patch4-window7-224](https://huggingface.co/microsoft/swin-tiny-patch4-window7-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1012
- Accuracy: 0.9647
- F1: 0.9647
- Recall: 0.9647
- Precision: 0.9647

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.4856        | 0.99  | 83   | 0.3771          | 0.8444   | 0.8444 | 0.8444 | 0.8444    |
| 0.3495        | 1.99  | 166  | 0.2608          | 0.8949   | 0.8949 | 0.8949 | 0.8949    |
| 0.252         | 2.99  | 249  | 0.1445          | 0.9487   | 0.9487 | 0.9487 | 0.9487    |
| 0.2364        | 3.99  | 332  | 0.1029          | 0.9588   | 0.9588 | 0.9588 | 0.9588    |
| 0.2178        | 4.99  | 415  | 0.1012          | 0.9647   | 0.9647 | 0.9647 | 0.9647    |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.1
