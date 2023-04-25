---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: transformers-qa
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# transformers-qa

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.9300
- Validation Loss: 1.1437
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
- optimizer: {'name': 'Adam', 'learning_rate': 5e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.5145     | 1.1500          | 0     |
| 0.9300     | 1.1437          | 1     |


### Framework versions

- Transformers 4.16.0.dev0
- TensorFlow 2.6.0
- Datasets 1.16.2.dev0
- Tokenizers 0.10.3
