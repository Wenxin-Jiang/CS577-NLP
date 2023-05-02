---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Zynovia/vit-base-patch16-224-in21k-wwwwii
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Zynovia/vit-base-patch16-224-in21k-wwwwii

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.8976
- Train Accuracy: 0.8813
- Train Top-3-accuracy: 0.9721
- Validation Loss: 1.6144
- Validation Accuracy: 0.5845
- Validation Top-3-accuracy: 0.7845
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 6e-05, 'decay_steps': 4122, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.001}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 3.4972     | 0.1475         | 0.3067               | 3.0825          | 0.3240              | 0.5178                    | 0     |
| 2.7352     | 0.4129         | 0.6613               | 2.4838          | 0.4543              | 0.6930                    | 1     |
| 2.0429     | 0.6153         | 0.8315               | 1.9934          | 0.5690              | 0.7550                    | 2     |
| 1.4246     | 0.7672         | 0.9166               | 1.6714          | 0.5876              | 0.8016                    | 3     |
| 0.8976     | 0.8813         | 0.9721               | 1.6144          | 0.5845              | 0.7845                    | 4     |


### Framework versions

- Transformers 4.21.2
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
