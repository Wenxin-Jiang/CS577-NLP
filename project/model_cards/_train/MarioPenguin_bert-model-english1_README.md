---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: bert-model-english1
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# bert-model-english1

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0274
- Train Accuracy: 0.9914
- Validation Loss: 0.3493
- Validation Accuracy: 0.9303
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
| 0.0366     | 0.9885         | 0.3013          | 0.9299              | 0     |
| 0.0261     | 0.9912         | 0.3445          | 0.9351              | 1     |
| 0.0274     | 0.9914         | 0.3493          | 0.9303              | 2     |


### Framework versions

- Transformers 4.16.2
- TensorFlow 2.7.0
- Datasets 1.18.3
- Tokenizers 0.11.0
