---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: europython-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# europython-imdb

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1279
- Train Accuracy: 0.9548
- Validation Loss: 0.1595
- Validation Accuracy: 0.9418
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
- optimizer: {'name': 'Adam', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.2073     | 0.9203         | 0.1486          | 0.9435              | 0     |
| 0.1279     | 0.9548         | 0.1595          | 0.9418              | 1     |


### Framework versions

- Transformers 4.21.0.dev0
- TensorFlow 2.9.1
- Datasets 2.3.3.dev0
- Tokenizers 0.11.0
