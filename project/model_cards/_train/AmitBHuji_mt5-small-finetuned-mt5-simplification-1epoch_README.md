---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: AmitBHuji/mt5-small-finetuned-mt5-simplification-1epoch
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# AmitBHuji/mt5-small-finetuned-mt5-simplification-1epoch

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 6.2240
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 1192, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Epoch |
|:----------:|:-----:|
| 15.1244    | 0     |
| 9.6794     | 1     |
| 7.9758     | 2     |
| 7.1858     | 3     |
| 6.6506     | 4     |
| 6.5284     | 5     |
| 6.2093     | 6     |
| 6.2240     | 7     |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1
