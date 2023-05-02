---
tags:
- generated_from_keras_callback
model-index:
- name: W4nkel/my_awesome_model
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# W4nkel/my_awesome_model

This model is a fine-tuned version of [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.3000
- Validation Loss: 0.3434
- Train Accuracy: 0.8658
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
- optimizer: {'name': 'Adam', 'weight_decay': None, 'clipnorm': None, 'global_clipnorm': None, 'clipvalue': None, 'use_ema': False, 'ema_momentum': 0.99, 'ema_overwrite_frequency': None, 'jit_compile': False, 'is_legacy_optimizer': False, 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 1500, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Accuracy | Epoch |
|:----------:|:---------------:|:--------------:|:-----:|
| 0.6644     | 0.4291          | 0.81           | 0     |
| 0.4185     | 0.3783          | 0.8425         | 1     |
| 0.3000     | 0.3434          | 0.8658         | 2     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.11.0
- Datasets 2.8.0
- Tokenizers 0.13.2
