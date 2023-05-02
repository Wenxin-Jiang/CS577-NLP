---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: trialz
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trialz

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0043

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

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 282  | 2.1342          |
| 2.308         | 2.0   | 564  | 2.0320          |
| 2.308         | 3.0   | 846  | 2.0148          |
| 2.1411        | 4.0   | 1128 | 2.0076          |
| 2.1411        | 5.0   | 1410 | 2.0043          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.12.1
