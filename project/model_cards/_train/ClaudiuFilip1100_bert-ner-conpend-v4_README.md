---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: bert-ner-conpend-v4
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# bert-ner-conpend-v4

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.3032
- Validation Loss: 0.2863
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 730, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.1871     | 0.9572          | 0     |
| 0.8742     | 0.7797          | 1     |
| 0.6743     | 0.5410          | 2     |
| 0.5184     | 0.4627          | 3     |
| 0.4239     | 0.3933          | 4     |
| 0.3739     | 0.3467          | 5     |
| 0.3456     | 0.3155          | 6     |
| 0.3277     | 0.3036          | 7     |
| 0.3099     | 0.2967          | 8     |
| 0.3032     | 0.2863          | 9     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.10.0
- Datasets 2.6.1
- Tokenizers 0.13.2
