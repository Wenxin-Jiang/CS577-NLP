---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: serverless-roomsort
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# serverless-roomsort

This model is a fine-tuned version of [microsoft/beit-base-patch16-224-pt22k-ft22k](https://huggingface.co/microsoft/beit-base-patch16-224-pt22k-ft22k) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0394
- Accuracy: 0.9892

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7844        | 1.0   | 762  | 0.0608          | 0.9791   |
| 0.0361        | 2.0   | 1524 | 0.0626          | 0.9830   |
| 0.0149        | 3.0   | 2286 | 0.0468          | 0.9879   |
| 0.0027        | 4.0   | 3048 | 0.0394          | 0.9892   |
| 0.0017        | 5.0   | 3810 | 0.0486          | 0.9889   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.13.0
