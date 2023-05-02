---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: tmp9wqcuxrt
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# tmp9wqcuxrt

This model is a fine-tuned version of [distilbert-base-german-cased](https://huggingface.co/distilbert-base-german-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.5063
- Train Accuracy: 0.7504
- Validation Loss: 0.5184
- Validation Accuracy: 0.7063
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 411, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.5067     | 0.7494         | 0.4881          | 0.7437              | 0     |
| 0.5063     | 0.7504         | 0.5184          | 0.7063              | 1     |


### Framework versions

- Transformers 4.21.2
- TensorFlow 2.8.2
- Datasets 2.2.2
- Tokenizers 0.12.1
