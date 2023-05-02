---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: FelipeAD/mt5-small-SENTENCE_COMPRESSION
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# FelipeAD/mt5-small-SENTENCE_COMPRESSION

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.1433
- Validation Loss: 0.9768
- Epoch: 3

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 179848, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 2.6046     | 1.1992          | 0     |
| 1.3586     | 1.0826          | 1     |
| 1.2178     | 1.0241          | 2     |
| 1.1433     | 0.9768          | 3     |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.6.0
- Datasets 2.3.2
- Tokenizers 0.12.1
