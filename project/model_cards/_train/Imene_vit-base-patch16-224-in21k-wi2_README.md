---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-224-in21k-wi2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-224-in21k-wi2

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.9892
- Train Accuracy: 0.5568
- Train Top-3-accuracy: 0.8130
- Validation Loss: 3.0923
- Validation Accuracy: 0.4280
- Validation Top-3-accuracy: 0.7034
- Epoch: 4

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 500, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 3.8488     | 0.0720         | 0.1713               | 3.7116          | 0.1564              | 0.3617                    | 0     |
| 3.5246     | 0.2703         | 0.4898               | 3.4122          | 0.3217              | 0.5732                    | 1     |
| 3.2493     | 0.4150         | 0.6827               | 3.2232          | 0.3880              | 0.6633                    | 2     |
| 3.0840     | 0.5002         | 0.7670               | 3.1275          | 0.4255              | 0.6921                    | 3     |
| 2.9892     | 0.5568         | 0.8130               | 3.0923          | 0.4280              | 0.7034                    | 4     |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
