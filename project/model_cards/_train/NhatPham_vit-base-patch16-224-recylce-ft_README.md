---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: vit-base-patch16-224
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->
# ## labels
- 0: Object
- 1: Recycle
- 2: Non-Recycle 


# vit-base-patch16-224

This model is a fine-tuned version of [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1510
- Accuracy: 0.9443

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
- train_batch_size: 60
- eval_batch_size: 60
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 240
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1438        | 1.0   | 150  | 0.1645          | 0.9353   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3
