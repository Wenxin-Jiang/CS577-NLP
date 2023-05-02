---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: NAOKITY/bert-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# NAOKITY/bert-squad

This model is a fine-tuned version of [pierreguillou/bert-base-cased-squad-v1.1-portuguese](https://huggingface.co/pierreguillou/bert-base-cased-squad-v1.1-portuguese) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.9778
- Validation Loss: 0.0
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 987, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.5286     | 0.0             | 0     |
| 0.9778     | 0.0             | 1     |


### Framework versions

- Transformers 4.20.0
- TensorFlow 2.9.1
- Datasets 2.3.2
- Tokenizers 0.12.1
