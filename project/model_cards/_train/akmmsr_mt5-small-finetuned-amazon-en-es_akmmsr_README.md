---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: akmmsr/mt5-small-finetuned-amazon-en-es_akmmsr
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# akmmsr/mt5-small-finetuned-amazon-en-es_akmmsr

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 4.0336
- Validation Loss: 3.3393
- Epoch: 7

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 9672, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 9.6397     | 4.2364          | 0     |
| 5.8621     | 3.7162          | 1     |
| 5.0948     | 3.5552          | 2     |
| 4.6724     | 3.4873          | 3     |
| 4.4007     | 3.4245          | 4     |
| 4.2162     | 3.3792          | 5     |
| 4.0985     | 3.3499          | 6     |
| 4.0336     | 3.3393          | 7     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.7.1
- Tokenizers 0.13.2
