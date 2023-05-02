---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: Raynok/roberta-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Raynok/roberta-squad

This model is a fine-tuned version of [Raynok/roberta-squad](https://huggingface.co/Raynok/roberta-squad) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.4731
- Epoch: 1

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 44284, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Epoch |
|:----------:|:-----:|
| 0.7257     | 0     |
| 0.4731     | 1     |


### Framework versions

- Transformers 4.19.3
- TensorFlow 2.9.1
- Datasets 2.3.2
- Tokenizers 0.12.1
