---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: my-awesome-model-2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# my-awesome-model-2

This model is a fine-tuned version of [dbmdz/bert-base-italian-cased](https://huggingface.co/dbmdz/bert-base-italian-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.2839
- Validation Loss: 0.2098
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 2e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': -969, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 1000, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.4575     | 0.2993          | 0     |
| 0.3525     | 0.2577          | 1     |
| 0.2839     | 0.2098          | 2     |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.9.0
- Datasets 2.2.2
- Tokenizers 0.12.1
