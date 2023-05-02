---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: YKXBCi/vit-base-patch16-224-in21k-euroSat
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# YKXBCi/vit-base-patch16-224-in21k-euroSat

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0495
- Train Accuracy: 0.9948
- Train Top-3-accuracy: 0.9999
- Validation Loss: 0.0782
- Validation Accuracy: 0.9839
- Validation Top-3-accuracy: 1.0
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 3585, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 0.4593     | 0.9478         | 0.9912               | 0.1558          | 0.9809              | 0.9995                    | 0     |
| 0.1008     | 0.9876         | 0.9997               | 0.0855          | 0.9856              | 1.0                       | 1     |
| 0.0495     | 0.9948         | 0.9999               | 0.0782          | 0.9839              | 1.0                       | 2     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.6.0
- Datasets 2.1.0
- Tokenizers 0.12.1
