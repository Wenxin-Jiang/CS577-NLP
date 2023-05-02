---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Nitika/distilbert-base-uncased-finetuned-cola
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Nitika/distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1924
- Validation Loss: 0.4890
- Train Matthews Correlation: 0.5406
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 2670, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Matthews Correlation | Epoch |
|:----------:|:---------------:|:--------------------------:|:-----:|
| 0.5210     | 0.4510          | 0.4918                     | 0     |
| 0.3327     | 0.4885          | 0.5156                     | 1     |
| 0.1924     | 0.4890          | 0.5406                     | 2     |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.2
- Datasets 2.2.2
- Tokenizers 0.12.1
