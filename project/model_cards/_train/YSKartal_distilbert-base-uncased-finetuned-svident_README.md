---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: YSKartal/distilbert-base-uncased-finetuned-svident
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# YSKartal/distilbert-base-uncased-finetuned-svident

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.2047
- Validation Loss: 0.4580
- Train F1: 0.7711
- Epoch: 2

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
| 0.3673     | 0.4657          | 0.6980   | 0     |
| 0.2394     | 0.4580          | 0.7711   | 1     |
| 0.2047     | 0.4580          | 0.7711   | 2     |


### Framework versions

- Transformers 4.22.0
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
