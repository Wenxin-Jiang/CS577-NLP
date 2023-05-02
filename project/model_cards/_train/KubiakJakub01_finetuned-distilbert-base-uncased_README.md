---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: KubiakJakub01/finetuned-distilbert-base-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# KubiakJakub01/finetuned-distilbert-base-uncased

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.2767
- Validation Loss: 0.4326
- Train Accuracy: 0.8319
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 1140, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Accuracy | Epoch |
|:----------:|:---------------:|:--------------:|:-----:|
| 0.4680     | 0.4008          | 0.8378         | 0     |
| 0.3475     | 0.4017          | 0.8385         | 1     |
| 0.2767     | 0.4326          | 0.8319         | 2     |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.9.1
- Datasets 2.4.0
- Tokenizers 0.12.1
