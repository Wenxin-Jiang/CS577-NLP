---
tags:
- generated_from_keras_callback
model-index:
- name: Boglinger/mt5-small-german-finetune-mlsum-klexv2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Boglinger/mt5-small-german-finetune-mlsum-klexv2

This model is a fine-tuned version of [ml6team/mt5-small-german-finetune-mlsum](https://huggingface.co/ml6team/mt5-small-german-finetune-mlsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.5577
- Validation Loss: 3.2091
- Epoch: 9

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 2280, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 4.0493     | 3.4725          | 0     |
| 3.8299     | 3.3641          | 1     |
| 3.7296     | 3.3059          | 2     |
| 3.6650     | 3.2651          | 3     |
| 3.6235     | 3.2407          | 4     |
| 3.5919     | 3.2227          | 5     |
| 3.5733     | 3.2122          | 6     |
| 3.5597     | 3.2091          | 7     |
| 3.5599     | 3.2091          | 8     |
| 3.5577     | 3.2091          | 9     |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.2
- Tokenizers 0.12.1
