---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- image_folder
metrics:
- accuracy
model-index:
- name: beit-base-patch16-224-pt22k-ft22k-finetuned-FER2013CKPlus-7e-05
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
      value: 1.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# beit-base-patch16-224-pt22k-ft22k-finetuned-FER2013CKPlus-7e-05

This model is a fine-tuned version of [lixiqi/beit-base-patch16-224-pt22k-ft22k-finetuned-FER2013-7e-05](https://huggingface.co/lixiqi/beit-base-patch16-224-pt22k-ft22k-finetuned-FER2013-7e-05) on the image_folder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0127
- Accuracy: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.9364        | 0.97  | 27   | 0.1873          | 0.9645   |
| 0.3365        | 1.97  | 54   | 0.0951          | 0.9848   |
| 0.2482        | 2.97  | 81   | 0.0562          | 0.9949   |
| 0.1844        | 3.97  | 108  | 0.0213          | 0.9949   |
| 0.1693        | 4.97  | 135  | 0.0127          | 1.0      |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
