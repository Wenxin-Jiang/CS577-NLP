---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-224-in21k-Writer-Identification
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-224-in21k-Writer-Identification

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.9065
- Train Accuracy: 0.6173
- Train Top-3-accuracy: 0.8384
- Validation Loss: 3.0602
- Validation Accuracy: 0.4255
- Validation Top-3-accuracy: 0.6884
- Epoch: 10

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 1e-05, 'decay_steps': 1500, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 3.8889     | 0.0401         | 0.0971               | 3.8524          | 0.0501              | 0.1577                    | 0     |
| 3.7785     | 0.1516         | 0.3210               | 3.7267          | 0.1464              | 0.3392                    | 1     |
| 3.6188     | 0.2656         | 0.4854               | 3.5946          | 0.2115              | 0.4143                    | 2     |
| 3.4631     | 0.3276         | 0.5860               | 3.4570          | 0.2728              | 0.5232                    | 3     |
| 3.3386     | 0.3959         | 0.6599               | 3.3664          | 0.3091              | 0.5757                    | 4     |
| 3.2366     | 0.4500         | 0.7094               | 3.2844          | 0.3342              | 0.5895                    | 5     |
| 3.1510     | 0.4879         | 0.7526               | 3.2364          | 0.3442              | 0.6170                    | 6     |
| 3.0757     | 0.5246         | 0.7823               | 3.1752          | 0.3830              | 0.6508                    | 7     |
| 3.0107     | 0.5612         | 0.8058               | 3.1281          | 0.4043              | 0.6596                    | 8     |
| 2.9549     | 0.5894         | 0.8212               | 3.0903          | 0.4255              | 0.6834                    | 9     |
| 2.9065     | 0.6173         | 0.8384               | 3.0602          | 0.4255              | 0.6884                    | 10    |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
