---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: transformers-abhi
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# transformers-abhi

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.9227
- Validation Loss: 2.5929
- Train Rougel: tf.Tensor(0.19853836, shape=(), dtype=float32)
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
- optimizer: {'name': 'Adam', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Rougel                                   | Epoch |
|:----------:|:---------------:|:----------------------------------------------:|:-----:|
| 2.9227     | 2.5929          | tf.Tensor(0.19853836, shape=(), dtype=float32) | 0     |


### Framework versions

- Transformers 4.20.0
- TensorFlow 2.9.2
- Datasets 2.8.0
- Tokenizers 0.12.1
