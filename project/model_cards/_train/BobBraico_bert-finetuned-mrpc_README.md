---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: bert-finetuned-mrpc
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# bert-finetuned-mrpc

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1719
- Train Accuracy: 0.9359
- Validation Loss: 0.4050
- Validation Accuracy: 0.8382
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 1374, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.5877     | 0.6823         | 0.4665          | 0.8015              | 0     |
| 0.3843     | 0.8201         | 0.4026          | 0.8309              | 1     |
| 0.1719     | 0.9359         | 0.4050          | 0.8382              | 2     |


### Framework versions

- Transformers 4.19.1
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1
