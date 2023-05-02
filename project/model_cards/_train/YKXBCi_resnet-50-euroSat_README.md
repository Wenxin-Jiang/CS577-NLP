---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: YKXBCi/resnet-50-euroSat
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# YKXBCi/resnet-50-euroSat

This model is a fine-tuned version of [microsoft/resnet-50](https://huggingface.co/microsoft/resnet-50) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1408
- Train Accuracy: 0.9540
- Train Top-3-accuracy: 0.9973
- Validation Loss: 0.2008
- Validation Accuracy: 0.9335
- Validation Top-3-accuracy: 0.9965
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 3585, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 0.8487     | 0.6969         | 0.9168               | 0.4793          | 0.8274              | 0.9802                    | 0     |
| 0.4363     | 0.8428         | 0.9845               | 0.3823          | 0.8641              | 0.9881                    | 1     |
| 0.3123     | 0.8863         | 0.9922               | 0.2945          | 0.8988              | 0.9928                    | 2     |
| 0.2153     | 0.9259         | 0.9952               | 0.2316          | 0.9187              | 0.9958                    | 3     |
| 0.1408     | 0.9540         | 0.9973               | 0.2008          | 0.9335              | 0.9965                    | 4     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.6.0
- Datasets 2.1.0
- Tokenizers 0.12.1
