---
tags:
- generated_from_keras_callback
model-index:
- name: Farras/mT5_multilingual_XLSum-kompas
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Farras/mT5_multilingual_XLSum-kompas

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 4.2318
- Validation Loss: 3.9491
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 920, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 4.6000     | 4.0879          | 0     |
| 4.2318     | 3.9491          | 1     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.10.0
- Datasets 2.7.1
- Tokenizers 0.13.2
