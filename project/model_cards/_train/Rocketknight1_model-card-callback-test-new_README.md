---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Rocketknight1/model-card-callback-test-new
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Rocketknight1/model-card-callback-test-new

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0031
- Train Accuracy: 1.0
- Validation Loss: 0.0000
- Validation Accuracy: 1.0
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
- optimizer: {'name': 'Adam', 'learning_rate': 0.001, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.4647     | 0.6406         | 0.0057          | 1.0                 | 0     |
| 0.0031     | 1.0            | 0.0000          | 1.0                 | 1     |


### Framework versions

- Transformers 4.14.0.dev0
- TensorFlow 2.6.0
- Datasets 1.16.2.dev0
- Tokenizers 0.10.3
