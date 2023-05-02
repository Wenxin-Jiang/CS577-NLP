---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: ParulChaudhari/distilbert-base-uncased-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# ParulChaudhari/distilbert-base-uncased-finetuned-squad

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an SQUAD dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.3927
- Validation Loss: 1.1305
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 177048, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.3927     | 1.1305          | 0     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.5.0
- Datasets 2.0.0
- Tokenizers 0.12.1
