---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: HuggingAlex1247/gelectra-large-germaner
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# HuggingAlex1247/gelectra-large-germaner

This model is a fine-tuned version of [deepset/gelectra-large](https://huggingface.co/deepset/gelectra-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1696
- Validation Loss: 0.0800
- Epoch: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 3475, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.1696     | 0.0800          | 0     |


### Framework versions

- Transformers 4.22.2
- TensorFlow 2.6.2
- Datasets 1.18.0
- Tokenizers 0.12.1
