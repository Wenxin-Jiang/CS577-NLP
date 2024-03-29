---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: JustAdvanceTechonology/medical_notes_mulitilingual
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# JustAdvanceTechonology/medical_notes_mulitilingual

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 8.7536
- Validation Loss: 6.1397
- Epoch: 7

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 1209, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 11.2097    | 6.1454          | 0     |
| 8.7069     | 6.1880          | 1     |
| 8.7350     | 6.1834          | 2     |
| 8.7021     | 6.1364          | 3     |
| 8.7385     | 6.2117          | 4     |
| 8.7318     | 6.2004          | 5     |
| 8.7487     | 6.1531          | 6     |
| 8.7536     | 6.1397          | 7     |


### Framework versions

- Transformers 4.16.2
- TensorFlow 2.5.0
- Datasets 2.0.0
- Tokenizers 0.10.1
