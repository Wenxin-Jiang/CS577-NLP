---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Anthos23/distilbert-base-uncased-finetuned-sst2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Anthos23/distilbert-base-uncased-finetuned-sst2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0662
- Validation Loss: 0.2623
- Train Accuracy: 0.9083
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 21045, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Accuracy | Epoch |
|:----------:|:---------------:|:--------------:|:-----:|
| 0.2101     | 0.2373          | 0.9083         | 0     |
| 0.1065     | 0.2645          | 0.9060         | 1     |
| 0.0662     | 0.2623          | 0.9083         | 2     |


### Framework versions

- Transformers 4.17.0.dev0
- TensorFlow 2.5.0
- Datasets 1.18.3
- Tokenizers 0.11.0
