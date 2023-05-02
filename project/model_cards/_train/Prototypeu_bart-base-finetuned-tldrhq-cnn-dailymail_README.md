---
tags:
- generated_from_keras_callback
model-index:
- name: Prototypeu/bart-base-finetuned-tldrhq-cnn-dailymail
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Prototypeu/bart-base-finetuned-tldrhq-cnn-dailymail

This model is a fine-tuned version of [Prototypeu/bart-base-finetuned-xsum](https://huggingface.co/Prototypeu/bart-base-finetuned-xsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.5049
- Train Logits Loss: 1.5049
- Train Rouge1: 28.1795
- Train Rouge2: 14.0392
- Train Rougel: 23.7617
- Train Rougelsum: 26.5583
- Train Gen Len: 19.0
- Epoch: 4

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 3e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 255113, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 32000, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.98, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Train Logits Loss | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Train Gen Len | Epoch |
|:----------:|:-----------------:|:------------:|:------------:|:------------:|:---------------:|:-------------:|:-----:|
| 2.9074     | 2.9074            | 26.9164      | 12.6984      | 22.4321      | 25.2287         | 19.0          | 0     |
| 1.9368     | 1.9368            | 28.0165      | 13.8906      | 23.4187      | 26.3779         | 19.0          | 1     |
| 1.7246     | 1.7246            | 27.6022      | 13.5255      | 23.2301      | 25.9923         | 19.0          | 2     |
| 1.5945     | 1.5945            | 28.0347      | 13.7045      | 23.4851      | 26.3488         | 19.0          | 3     |
| 1.5049     | 1.5049            | 28.1795      | 14.0392      | 23.7617      | 26.5583         | 19.0          | 4     |


### Framework versions

- Transformers 4.17.0
- TensorFlow 2.6.0
- Datasets 2.0.0
- Tokenizers 0.11.6
