---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: SiriRRR/bart-base-finetuned-test
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# SiriRRR/bart-base-finetuned-test

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.5900
- Validation Loss: 2.6982
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 2864, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 2.4667     | 2.1935          | 0     |
| 1.7786     | 2.2691          | 1     |
| 1.4244     | 2.3324          | 2     |
| 1.1479     | 2.4362          | 3     |
| 0.9405     | 2.5442          | 4     |
| 0.7770     | 2.5797          | 5     |
| 0.6615     | 2.6505          | 6     |
| 0.5900     | 2.6982          | 7     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.7.1
- Tokenizers 0.13.2
