---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Boglinger/mt5-small-klex
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Boglinger/mt5-small-klex

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 4.7908
- Validation Loss: 3.2086
- Epoch: 19

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 2344, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 10.4780    | 4.4037          | 0     |
| 6.5474     | 3.8111          | 1     |
| 5.7133     | 3.5425          | 2     |
| 5.3385     | 3.3847          | 3     |
| 5.0827     | 3.3011          | 4     |
| 4.9326     | 3.2479          | 5     |
| 4.8377     | 3.2185          | 6     |
| 4.7692     | 3.2086          | 7     |
| 4.7478     | 3.2086          | 8     |
| 4.7534     | 3.2086          | 9     |
| 4.7665     | 3.2086          | 10    |
| 4.7779     | 3.2086          | 11    |
| 4.7689     | 3.2086          | 12    |
| 4.7838     | 3.2086          | 13    |
| 4.7881     | 3.2086          | 14    |
| 4.7869     | 3.2086          | 15    |
| 4.7612     | 3.2086          | 16    |
| 4.7667     | 3.2086          | 17    |
| 4.7581     | 3.2086          | 18    |
| 4.7908     | 3.2086          | 19    |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1
