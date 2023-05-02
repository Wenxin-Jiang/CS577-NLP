---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mbti-classification-xlnet-base-cased-augment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbti-classification-xlnet-base-cased-augment

This model is a fine-tuned version of [xlnet-base-cased](https://huggingface.co/xlnet-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2045
- Accuracy: 0.2829

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
- lr_scheduler_type: cosine
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Accuracy | Validation Loss |
|:-------------:|:-----:|:-----:|:--------:|:---------------:|
| 2.1055        | 1.0   | 29900 | 0.2884   | 2.1344          |
| 1.8127        | 2.0   | 59800 | 0.2830   | 2.1479          |
| 1.6953        | 3.0   | 89700 | 2.2045   | 0.2829          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
