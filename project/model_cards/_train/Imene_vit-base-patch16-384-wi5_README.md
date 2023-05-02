---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-384-wi5
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-384-wi5

This model is a fine-tuned version of [google/vit-base-patch16-384](https://huggingface.co/google/vit-base-patch16-384) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.4102
- Train Accuracy: 0.9755
- Train Top-3-accuracy: 0.9960
- Validation Loss: 1.9021
- Validation Accuracy: 0.4912
- Validation Top-3-accuracy: 0.7302
- Epoch: 8

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 3180, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 4.2945     | 0.0568         | 0.1328               | 3.6233          | 0.1387              | 0.2916                    | 0     |
| 3.1234     | 0.2437         | 0.4585               | 2.8657          | 0.3041              | 0.5330                    | 1     |
| 2.4383     | 0.4182         | 0.6638               | 2.5499          | 0.3534              | 0.6048                    | 2     |
| 1.9258     | 0.5698         | 0.7913               | 2.3046          | 0.4202              | 0.6583                    | 3     |
| 1.4919     | 0.6963         | 0.8758               | 2.1349          | 0.4553              | 0.6784                    | 4     |
| 1.1127     | 0.7992         | 0.9395               | 2.0878          | 0.4595              | 0.6809                    | 5     |
| 0.8092     | 0.8889         | 0.9720               | 1.9460          | 0.4962              | 0.7210                    | 6     |
| 0.5794     | 0.9419         | 0.9883               | 1.9478          | 0.4979              | 0.7201                    | 7     |
| 0.4102     | 0.9755         | 0.9960               | 1.9021          | 0.4912              | 0.7302                    | 8     |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
