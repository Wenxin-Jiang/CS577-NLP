---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: philschmid/tf-distilbart-cnn-12-6-tradetheevent
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# philschmid/tf-distilbart-cnn-12-6-tradetheevent

This model is a fine-tuned version of [philschmid/tf-distilbart-cnn-12-6](https://huggingface.co/philschmid/tf-distilbart-cnn-12-6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.6894
- Validation Loss: 1.7245
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 161440, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.6635     | 1.5957          | 0     |
| 1.3144     | 1.5577          | 1     |
| 1.0819     | 1.6059          | 2     |
| 0.8702     | 1.6695          | 3     |
| 0.6894     | 1.7245          | 4     |


### Framework versions

- Transformers 4.16.0.dev0
- TensorFlow 2.7.0
- Datasets 1.17.0
- Tokenizers 0.10.3
