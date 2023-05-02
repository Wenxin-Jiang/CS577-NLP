---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: OMARS200/primer_modelo_hub
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# OMARS200/primer_modelo_hub

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0892
- Validation Loss: 0.6573
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.1565     | 0.6118          | 0     |
| 0.0892     | 0.6573          | 1     |


### Framework versions

- Transformers 4.21.0
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
