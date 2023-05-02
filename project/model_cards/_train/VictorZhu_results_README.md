---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1194

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.1428        | 1.0   | 510  | 0.1347          |
| 0.0985        | 2.0   | 1020 | 0.1189          |
| 0.0763        | 3.0   | 1530 | 0.1172          |
| 0.0646        | 4.0   | 2040 | 0.1194          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu102
- Datasets 2.2.2
- Tokenizers 0.12.1
