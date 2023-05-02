---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: HanSSH/mt5-small-finetuned-amazon-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# HanSSH/mt5-small-finetuned-amazon-en-es

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.2684
- Validation Loss: 3.2288
- Epoch: 3

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 0.00056, 'decay_steps': 4836, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 5.8144     | 3.5283          | 0     |
| 3.8758     | 3.2971          | 1     |
| 3.4741     | 3.2452          | 2     |
| 3.2684     | 3.2288          | 3     |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.10.0
- Datasets 2.4.0
- Tokenizers 0.12.1
