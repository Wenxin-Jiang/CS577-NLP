---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: test_trainer_XLNET_3ep_5e-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test_trainer_XLNET_3ep_5e-5

This model is a fine-tuned version of [xlnet-base-cased](https://huggingface.co/xlnet-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5405
- Accuracy: 0.8773

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7984        | 1.0   | 1125 | 0.6647          | 0.7923   |
| 0.5126        | 2.0   | 2250 | 0.4625          | 0.862    |
| 0.409         | 3.0   | 3375 | 0.5405          | 0.8773   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
