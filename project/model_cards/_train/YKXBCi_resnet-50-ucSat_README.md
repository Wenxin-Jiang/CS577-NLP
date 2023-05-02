---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: YKXBCi/resnet-50-ucSat
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# YKXBCi/resnet-50-ucSat

This model is a fine-tuned version of [microsoft/resnet-50](https://huggingface.co/microsoft/resnet-50) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.9091
- Train Accuracy: 0.7125
- Train Top-3-accuracy: 0.9227
- Validation Loss: 1.0869
- Validation Accuracy: 0.6562
- Validation Top-3-accuracy: 0.8924
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
| 2.6504     | 0.2057         | 0.3591               | 2.2693          | 0.3299              | 0.5069                    | 0     |
| 1.8871     | 0.4062         | 0.6494               | 1.6561          | 0.4618              | 0.7083                    | 1     |
| 1.4603     | 0.5278         | 0.7790               | 1.4162          | 0.5417              | 0.8021                    | 2     |
| 1.1499     | 0.6199         | 0.8676               | 1.2030          | 0.625               | 0.8646                    | 3     |
| 0.9091     | 0.7125         | 0.9227               | 1.0869          | 0.6562              | 0.8924                    | 4     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.6.0
- Datasets 2.1.0
- Tokenizers 0.12.1
