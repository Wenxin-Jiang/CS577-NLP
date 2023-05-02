---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9229
- Accuracy: 0.7586

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.9119        | 1.0   | 258  | 0.8750          | 0.7241   |
| 0.8307        | 2.0   | 516  | 0.9229          | 0.7586   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
