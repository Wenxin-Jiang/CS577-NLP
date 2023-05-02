---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: ajdowney/bert-wash-binary-25
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# ajdowney/bert-wash-binary-25

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.3261
- Validation Loss: 0.6889
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 129, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.4722     | 0.5900          | 0     |
| 0.3985     | 0.6213          | 1     |
| 0.3261     | 0.6889          | 2     |


### Framework versions

- Transformers 4.23.1
- TensorFlow 2.10.0
- Datasets 2.6.1
- Tokenizers 0.13.1
