---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta-base-bne-finetuned-mnli
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-bne-finetuned-mnli

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2869
- Accuracy: 0.9012

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.3222        | 1.0   | 1255 | 0.2869          | 0.9012   |
| 0.2418        | 2.0   | 2510 | 0.3125          | 0.8987   |
| 0.1726        | 3.0   | 3765 | 0.4120          | 0.8943   |
| 0.0685        | 4.0   | 5020 | 0.5239          | 0.8919   |
| 0.0245        | 5.0   | 6275 | 0.5910          | 0.8947   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.12.1
- Tokenizers 0.10.3
