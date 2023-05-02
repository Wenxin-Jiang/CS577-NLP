---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Arandine/bert-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Arandine/bert-finetuned-squad

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.5695
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 16638, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Epoch |
|:----------:|:-----:|
| 1.2752     | 0     |
| 0.7798     | 1     |
| 0.5695     | 2     |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1
