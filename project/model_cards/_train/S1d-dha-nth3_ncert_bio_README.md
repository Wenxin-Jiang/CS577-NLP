---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: S1d-dha-nth3/ncert_bio
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# S1d-dha-nth3/ncert_bio

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.6150
- Validation Loss: 2.5873
- Epoch: 14

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 2e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': -647, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 1000, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 3.5434     | 2.8928          | 0     |
| 2.9142     | 2.6476          | 1     |
| 2.6884     | 2.5008          | 2     |
| 2.6079     | 2.5775          | 3     |
| 2.5748     | 2.5737          | 4     |
| 2.6031     | 2.5074          | 5     |
| 2.6237     | 2.5028          | 6     |
| 2.5849     | 2.5862          | 7     |
| 2.6154     | 2.4751          | 8     |
| 2.5584     | 2.4866          | 9     |
| 2.6107     | 2.5268          | 10    |
| 2.5852     | 2.5659          | 11    |
| 2.5915     | 2.5768          | 12    |
| 2.5678     | 2.7020          | 13    |
| 2.6150     | 2.5873          | 14    |


### Framework versions

- Transformers 4.22.1
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
