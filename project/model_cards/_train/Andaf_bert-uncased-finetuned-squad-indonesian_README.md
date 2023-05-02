---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: Andaf/chatbot-trvlk-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Andaf/chatbot-trvlk-finetuned-squad

This model is a fine-tuned version of [cahya/bert-base-indonesian-522M](https://huggingface.co/cahya/bert-base-indonesian-522M) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.5335
- Validation Loss: 6.4566
- Epoch: 1

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 14444, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 2.1851     | 6.1907          | 0     |
| 1.5335     | 6.4566          | 1     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.8.1
- Tokenizers 0.12.1
