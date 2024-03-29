---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta-base-ca-finetuned-mnli
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-ca-finetuned-mnli

This model is a fine-tuned version of [BSC-TeMU/roberta-base-ca](https://huggingface.co/BSC-TeMU/roberta-base-ca) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4137
- Accuracy: 0.8778

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
| 0.3699        | 1.0   | 1255 | 0.3712          | 0.8669   |
| 0.3082        | 2.0   | 2510 | 0.3401          | 0.8766   |
| 0.2375        | 3.0   | 3765 | 0.4137          | 0.8778   |
| 0.1889        | 4.0   | 5020 | 0.4671          | 0.8733   |
| 0.1486        | 5.0   | 6275 | 0.5205          | 0.8749   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.12.1
- Tokenizers 0.10.3
