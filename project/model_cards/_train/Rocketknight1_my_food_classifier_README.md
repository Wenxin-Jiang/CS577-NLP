---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Rocketknight1/my_food_classifier
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Rocketknight1/my_food_classifier

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1099
- Validation Loss: 0.2439
- Train Accuracy: 0.947
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 20000, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Accuracy | Epoch |
|:----------:|:---------------:|:--------------:|:-----:|
| 2.5330     | 1.3738          | 0.923          | 0     |
| 0.8871     | 0.6131          | 0.95           | 1     |
| 0.3703     | 0.4042          | 0.937          | 2     |
| 0.1942     | 0.2981          | 0.94           | 3     |
| 0.1099     | 0.2439          | 0.947          | 4     |


### Framework versions

- Transformers 4.26.0.dev0
- TensorFlow 2.11.0
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
