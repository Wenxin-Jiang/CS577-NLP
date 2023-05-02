---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-384-wi3
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-384-wi3

This model is a fine-tuned version of [google/vit-base-patch16-384](https://huggingface.co/google/vit-base-patch16-384) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.2020
- Train Accuracy: 0.9984
- Train Top-3-accuracy: 0.9997
- Validation Loss: 1.4297
- Validation Accuracy: 0.6195
- Validation Top-3-accuracy: 0.8298
- Epoch: 11

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 1200, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 3.6575     | 0.0902         | 0.1945               | 3.1772          | 0.2028              | 0.3980                    | 0     |
| 2.5870     | 0.3473         | 0.6048               | 2.3845          | 0.3717              | 0.6208                    | 1     |
| 1.8813     | 0.5553         | 0.7895               | 2.0262          | 0.4431              | 0.7196                    | 2     |
| 1.4326     | 0.6815         | 0.8754               | 1.8856          | 0.4793              | 0.7384                    | 3     |
| 1.0572     | 0.7989         | 0.9439               | 1.6570          | 0.5369              | 0.7960                    | 4     |
| 0.7740     | 0.8838         | 0.9749               | 1.6103          | 0.5557              | 0.7960                    | 5     |
| 0.5593     | 0.9417         | 0.9900               | 1.5303          | 0.5695              | 0.8173                    | 6     |
| 0.4151     | 0.9709         | 0.9975               | 1.4939          | 0.5795              | 0.8185                    | 7     |
| 0.3176     | 0.9884         | 0.9978               | 1.4553          | 0.5832              | 0.8248                    | 8     |
| 0.2582     | 0.9950         | 0.9991               | 1.4500          | 0.6020              | 0.8248                    | 9     |
| 0.2222     | 0.9978         | 0.9994               | 1.4315          | 0.6108              | 0.8310                    | 10    |
| 0.2020     | 0.9984         | 0.9997               | 1.4297          | 0.6195              | 0.8298                    | 11    |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
