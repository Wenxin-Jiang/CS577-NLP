---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: YKXBCi/vit-base-patch16-224-in21k-ucSat
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# YKXBCi/vit-base-patch16-224-in21k-ucSat

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.3216
- Train Accuracy: 0.9960
- Train Top-3-accuracy: 1.0
- Validation Loss: 1.3683
- Validation Accuracy: 0.9688
- Validation Top-3-accuracy: 0.9931
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 275, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 2.7376     | 0.5375         | 0.7284               | 2.3789          | 0.8958              | 0.9757                    | 0     |
| 2.1030     | 0.9449         | 0.9972               | 1.8664          | 0.9479              | 0.9896                    | 1     |
| 1.6719     | 0.9812         | 1.0                  | 1.5763          | 0.9618              | 0.9931                    | 2     |
| 1.4357     | 0.9926         | 1.0                  | 1.4201          | 0.9688              | 0.9931                    | 3     |
| 1.3216     | 0.9960         | 1.0                  | 1.3683          | 0.9688              | 0.9931                    | 4     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.6.0
- Datasets 2.1.0
- Tokenizers 0.12.1
