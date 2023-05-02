---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vc-bantai-vit-withoutAMBI-adunest-trial
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      args: Violation-Classification---Raw-9
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7797741273100616
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vc-bantai-vit-withoutAMBI-adunest-trial

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4289
- Accuracy: 0.7798

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 0.4   | 100  | 1.0782          | 0.4451   |
| No log        | 0.8   | 200  | 0.5634          | 0.7156   |
| No log        | 1.2   | 300  | 0.7181          | 0.6684   |
| No log        | 1.61  | 400  | 0.4289          | 0.7798   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
