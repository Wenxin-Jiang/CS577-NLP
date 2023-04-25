---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Rocketknight1/distilbert-base-uncased-finetuned-cola
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Rocketknight1/distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.3182
- Validation Loss: 0.4914
- Train Matthews Correlation: 0.5056
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 1602, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Matthews Correlation | Epoch |
|:----------:|:---------------:|:--------------------------:|:-----:|
| 0.5126     | 0.4638          | 0.4555                     | 0     |
| 0.3182     | 0.4914          | 0.5056                     | 1     |


### Framework versions

- Transformers 4.22.0.dev0
- TensorFlow 2.9.1
- Datasets 2.4.1.dev0
- Tokenizers 0.11.0
