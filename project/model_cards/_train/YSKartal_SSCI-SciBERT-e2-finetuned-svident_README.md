---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: YSKartal/SSCI-SciBERT-e2-finetuned-svident
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# YSKartal/SSCI-SciBERT-e2-finetuned-svident

This model is a fine-tuned version of [KM4STfulltext/SSCI-SciBERT-e2](https://huggingface.co/KM4STfulltext/SSCI-SciBERT-e2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1916
- Validation Loss: 0.4552
- Train F1: 0.7665
- Epoch: 4

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 351, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train F1 | Epoch |
|:----------:|:---------------:|:--------:|:-----:|
| 0.1946     | 0.4552          | 0.7665   | 0     |
| 0.1944     | 0.4552          | 0.7665   | 1     |
| 0.1928     | 0.4552          | 0.7665   | 2     |
| 0.1963     | 0.4552          | 0.7665   | 3     |
| 0.1916     | 0.4552          | 0.7665   | 4     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.2
