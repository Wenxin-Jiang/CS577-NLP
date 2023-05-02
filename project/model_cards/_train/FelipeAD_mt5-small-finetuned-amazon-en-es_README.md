---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: FelipeAD/mt5-small-finetuned-amazon-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# FelipeAD/mt5-small-finetuned-amazon-en-es

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 4.0682
- Validation Loss: 3.3902
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
| 10.0232    | 4.5431          | 0     |
| 6.0233     | 3.9118          | 1     |
| 5.2216     | 3.6621          | 2     |
| 4.7560     | 3.5532          | 3     |
| 4.4685     | 3.4825          | 4     |
| 4.2748     | 3.4303          | 5     |
| 4.1432     | 3.4013          | 6     |
| 4.0682     | 3.3902          | 7     |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1
