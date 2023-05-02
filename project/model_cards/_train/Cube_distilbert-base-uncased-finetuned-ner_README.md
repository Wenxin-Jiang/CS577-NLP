---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Cube/distilbert-base-uncased-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Cube/distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0339
- Validation Loss: 0.0646
- Train Precision: 0.9217
- Train Recall: 0.9295
- Train F1: 0.9256
- Train Accuracy: 0.9827
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 2631, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Precision | Train Recall | Train F1 | Train Accuracy | Epoch |
|:----------:|:---------------:|:---------------:|:------------:|:--------:|:--------------:|:-----:|
| 0.1996     | 0.0735          | 0.8930          | 0.9179       | 0.9053   | 0.9784         | 0     |
| 0.0545     | 0.0666          | 0.9137          | 0.9292       | 0.9214   | 0.9817         | 1     |
| 0.0339     | 0.0646          | 0.9217          | 0.9295       | 0.9256   | 0.9827         | 2     |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.2
- Datasets 2.2.2
- Tokenizers 0.12.1
