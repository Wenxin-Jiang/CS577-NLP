---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Shobhank-iiitdwd/distilbert-base-uncased-finetuned-qqp
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Shobhank-iiitdwd/distilbert-base-uncased-finetuned-qqp

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.2919
- Validation Loss: 0.2551
- Train Accuracy: 0.8894
- Train F1: 0.8531
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 22740, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Accuracy | Train F1 | Epoch |
|:----------:|:---------------:|:--------------:|:--------:|:-----:|
| 0.2919     | 0.2551          | 0.8894         | 0.8531   | 0     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.2
- Datasets 2.8.0
- Tokenizers 0.13.2
