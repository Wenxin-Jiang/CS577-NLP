---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-224-in21k-wwwwii
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-224-in21k-wwwwii

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.8024
- Train Accuracy: 0.9939
- Train Top-3-accuracy: 0.9997
- Validation Loss: 1.6739
- Validation Accuracy: 0.6267
- Validation Top-3-accuracy: 0.8349
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 4e-05, 'decay_steps': 1620, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.001}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 3.6793     | 0.125          | 0.2805               | 3.4078          | 0.2151              | 0.4756                    | 0     |
| 3.1763     | 0.3448         | 0.6265               | 3.0167          | 0.4209              | 0.6640                    | 1     |
| 2.7546     | 0.5419         | 0.7852               | 2.6634          | 0.5326              | 0.7651                    | 2     |
| 2.3537     | 0.6855         | 0.8843               | 2.3971          | 0.5547              | 0.7860                    | 3     |
| 1.9989     | 0.7814         | 0.9279               | 2.2236          | 0.5837              | 0.7907                    | 4     |
| 1.6670     | 0.875          | 0.9698               | 2.0757          | 0.5977              | 0.7907                    | 5     |
| 1.3815     | 0.9352         | 0.9890               | 1.8921          | 0.6198              | 0.8174                    | 6     |
| 1.1407     | 0.9651         | 0.9956               | 1.7976          | 0.6244              | 0.8174                    | 7     |
| 0.9451     | 0.9866         | 0.9983               | 1.7227          | 0.6349              | 0.8267                    | 8     |
| 0.8024     | 0.9939         | 0.9997               | 1.6739          | 0.6267              | 0.8349                    | 9     |


### Framework versions

- Transformers 4.21.2
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
