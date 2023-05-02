---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: Ashraf-kasem/gpt2_fine_tune_uncleaned_ds
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Ashraf-kasem/gpt2_fine_tune_uncleaned_ds

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.1724
- Validation Loss: 3.9371
- Epoch: 5

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 147444, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 4.1003     | 4.0757          | 0     |
| 3.6090     | 3.9807          | 1     |
| 3.4057     | 3.9625          | 2     |
| 3.2859     | 3.9406          | 3     |
| 3.2125     | 3.9486          | 4     |
| 3.1724     | 3.9371          | 5     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.0
- Datasets 2.8.0
- Tokenizers 0.13.2
