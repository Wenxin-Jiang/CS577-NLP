---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Rocketknight1/bert-base-uncased-finetuned-swag
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Rocketknight1/bert-base-uncased-finetuned-swag

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.8360
- Train Accuracy: 0.6631
- Validation Loss: 0.5885
- Validation Accuracy: 0.7706
- Epoch: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 9192, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.8360     | 0.6631         | 0.5885          | 0.7706              | 0     |


### Framework versions

- Transformers 4.18.0.dev0
- TensorFlow 2.8.0-rc0
- Datasets 2.0.1.dev0
- Tokenizers 0.11.0
