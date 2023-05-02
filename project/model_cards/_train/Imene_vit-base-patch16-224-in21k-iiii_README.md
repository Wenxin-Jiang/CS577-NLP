---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-224-in21k-iiii
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-224-in21k-iiii

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.8947
- Train Accuracy: 0.5439
- Train Top-3-accuracy: 0.7916
- Validation Loss: 3.0482
- Validation Accuracy: 0.3907
- Validation Top-3-accuracy: 0.6302
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 540, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 3.8068     | 0.0843         | 0.2108               | 3.6116          | 0.1721              | 0.3593                    | 0     |
| 3.4497     | 0.2735         | 0.4840               | 3.3654          | 0.2779              | 0.4953                    | 1     |
| 3.1913     | 0.3991         | 0.6314               | 3.1839          | 0.3512              | 0.5977                    | 2     |
| 3.0017     | 0.4878         | 0.7311               | 3.0867          | 0.3872              | 0.6233                    | 3     |
| 2.8947     | 0.5439         | 0.7916               | 3.0482          | 0.3907              | 0.6302                    | 4     |


### Framework versions

- Transformers 4.21.2
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
