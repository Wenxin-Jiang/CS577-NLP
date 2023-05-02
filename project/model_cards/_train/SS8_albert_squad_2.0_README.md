---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: albert_squad_2.0
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# albert_squad_2.0

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.6320
- Validation Loss: 0.8542
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
- optimizer: {'name': 'LAMB', 'learning_rate': 3e-05, 'weight_decay': 0.0, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-06, 'exclude_from_weight_decay': None, 'exclude_from_layer_adaptation': None}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.1381     | 0.9066          | 0     |
| 0.7778     | 0.8423          | 1     |
| 0.6320     | 0.8542          | 2     |


### Framework versions

- Transformers 4.16.0.dev0
- TensorFlow 2.7.0
- Datasets 1.17.0
- Tokenizers 0.10.3
