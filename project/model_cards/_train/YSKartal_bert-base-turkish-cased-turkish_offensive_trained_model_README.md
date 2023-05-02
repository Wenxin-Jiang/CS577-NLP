---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: YSKartal/bert-base-turkish-cased-turkish_offensive_trained_model
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# YSKartal/bert-base-turkish-cased-turkish_offensive_trained_model

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on [offenseval2020_tr](https://huggingface.co/datasets/offenseval2020_tr) dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0365
- Validation Loss: 0.4846
- Train F1: 0.6993
- Epoch: 3

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 7936, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train F1 | Epoch |
|:----------:|:---------------:|:--------:|:-----:|
| 0.3003     | 0.2664          | 0.6971   | 0     |
| 0.1866     | 0.3018          | 0.6990   | 1     |
| 0.0860     | 0.3803          | 0.7032   | 2     |
| 0.0365     | 0.4846          | 0.6993   | 3     |


### Framework versions

- Transformers 4.23.1
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.1
