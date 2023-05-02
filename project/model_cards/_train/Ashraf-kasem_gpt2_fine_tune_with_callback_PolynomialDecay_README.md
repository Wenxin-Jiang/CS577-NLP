---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: Ashraf-kasem/gpt2_fine_tune_with_callback_PolynomialDecay
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Ashraf-kasem/gpt2_fine_tune_with_callback_PolynomialDecay

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.9746
- Train Accuracy: 0.0063
- Validation Loss: 4.3079
- Validation Accuracy: 0.0044
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 14676, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 4.6420     | 0.0092         | 4.4445          | 0.0056              | 0     |
| 4.1331     | 0.0067         | 4.3297          | 0.0047              | 1     |
| 3.9746     | 0.0063         | 4.3079          | 0.0044              | 2     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.0
- Datasets 2.8.0
- Tokenizers 0.13.2
