---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: YKXBCi/vit-base-patch16-224-in21k-aidSat
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# YKXBCi/vit-base-patch16-224-in21k-aidSat

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.4026
- Train Accuracy: 0.9981
- Train Top-3-accuracy: 0.9998
- Validation Loss: 0.4715
- Validation Accuracy: 0.9796
- Validation Top-3-accuracy: 0.9980
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 1325, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 2.3544     | 0.7383         | 0.8687               | 1.5415          | 0.9266              | 0.9857                    | 0     |
| 1.1313     | 0.9522         | 0.9942               | 0.8788          | 0.9613              | 0.9966                    | 1     |
| 0.6741     | 0.9841         | 0.9985               | 0.6268          | 0.9640              | 0.9986                    | 2     |
| 0.4785     | 0.9953         | 0.9995               | 0.5058          | 0.9755              | 0.9980                    | 3     |
| 0.4026     | 0.9981         | 0.9998               | 0.4715          | 0.9796              | 0.9980                    | 4     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.6.0
- Datasets 2.1.0
- Tokenizers 0.12.1
