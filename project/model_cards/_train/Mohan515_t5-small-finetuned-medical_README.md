---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Mohan515/t5-small-finetuned-medical
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Mohan515/t5-small-finetuned-medical

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.8018
- Validation Loss: 0.5835
- Train Rouge1: 43.3783
- Train Rouge2: 35.1091
- Train Rougel: 41.6332
- Train Rougelsum: 42.5743
- Train Gen Len: 17.4718
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Train Gen Len | Epoch |
|:----------:|:---------------:|:------------:|:------------:|:------------:|:---------------:|:-------------:|:-----:|
| 0.8018     | 0.5835          | 43.3783      | 35.1091      | 41.6332      | 42.5743         | 17.4718       | 0     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.7.0
- Tokenizers 0.13.2
