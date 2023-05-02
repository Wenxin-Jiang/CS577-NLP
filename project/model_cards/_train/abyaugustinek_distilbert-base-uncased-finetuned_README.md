---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: abyaugustinek/distilbert-base-uncased-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# abyaugustinek/distilbert-base-uncased-finetuned

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.3693
- Validation Loss: 1.2106
- Train Precision: 0.0
- Train Recall: 0.0
- Train F1: 0.0
- Train Accuracy: 0.6565
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 30, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Precision | Train Recall | Train F1 | Train Accuracy | Epoch |
|:----------:|:---------------:|:---------------:|:------------:|:--------:|:--------------:|:-----:|
| 2.0691     | 1.5942          | 0.0             | 0.0          | 0.0      | 0.6565         | 0     |
| 1.4705     | 1.2376          | 0.0             | 0.0          | 0.0      | 0.6565         | 1     |
| 1.3693     | 1.2106          | 0.0             | 0.0          | 0.0      | 0.6565         | 2     |


### Framework versions

- Transformers 4.21.0
- TensorFlow 2.7.0
- Datasets 2.3.2
- Tokenizers 0.12.1
