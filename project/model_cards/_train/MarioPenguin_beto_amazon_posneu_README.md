---
tags:
- generated_from_keras_callback
model-index:
- name: beto_amazon_posneu
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# beto_amazon_posneu

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-uncased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1277
- Train Accuracy: 0.9550
- Validation Loss: 0.3439
- Validation Accuracy: 0.8905
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
- optimizer: {'name': 'Adam', 'learning_rate': 5e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.3195     | 0.8712         | 0.3454          | 0.8580              | 0     |
| 0.1774     | 0.9358         | 0.3258          | 0.8802              | 1     |
| 0.1277     | 0.9550         | 0.3439          | 0.8905              | 2     |


### Framework versions

- Transformers 4.16.2
- TensorFlow 2.7.0
- Datasets 1.18.3
- Tokenizers 0.11.0
