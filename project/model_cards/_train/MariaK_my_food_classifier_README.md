---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: MariaK/my_food_classifier
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# MariaK/my_food_classifier

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1163
- Validation Loss: 0.2927
- Train Accuracy: 0.936
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
| 2.5557     | 1.4200          | 0.897          | 0     |
| 0.8928     | 0.6662          | 0.931          | 1     |
| 0.3831     | 0.4001          | 0.938          | 2     |
| 0.1892     | 0.3486          | 0.93           | 3     |
| 0.1163     | 0.2927          | 0.936          | 4     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.2
- Datasets 2.8.0
- Tokenizers 0.13.2
