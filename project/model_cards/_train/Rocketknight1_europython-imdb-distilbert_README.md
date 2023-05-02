---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: europython-imdb-distilbert
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# europython-imdb-distilbert

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.3081
- Train Accuracy: 0.8663
- Validation Loss: 0.2459
- Validation Accuracy: 0.9006
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

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.3081     | 0.8663         | 0.2459          | 0.9006              | 0     |


### Framework versions

- Transformers 4.21.0.dev0
- TensorFlow 2.9.1
- Datasets 2.3.3.dev0
- Tokenizers 0.11.0
