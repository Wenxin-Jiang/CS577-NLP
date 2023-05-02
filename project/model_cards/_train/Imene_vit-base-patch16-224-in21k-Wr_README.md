---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-224-in21k-Wr
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-224-in21k-Wr

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.3104
- Train Accuracy: 0.9956
- Train Top-3-accuracy: 0.9981
- Validation Loss: 1.6041
- Validation Accuracy: 0.5770
- Validation Top-3-accuracy: 0.8035
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 0.0001, 'decay_steps': 1500, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 3.8300     | 0.0583         | 0.1381               | 3.6801          | 0.0951              | 0.2203                    | 0     |
| 3.2915     | 0.2418         | 0.4557               | 3.0277          | 0.3004              | 0.5507                    | 1     |
| 2.6535     | 0.4438         | 0.7106               | 2.5932          | 0.3780              | 0.6546                    | 2     |
| 2.0541     | 0.6308         | 0.8575               | 2.2998          | 0.4556              | 0.6871                    | 3     |
| 1.4622     | 0.7924         | 0.9496               | 2.0054          | 0.5056              | 0.7234                    | 4     |
| 0.9098     | 0.9201         | 0.9887               | 1.8079          | 0.5695              | 0.7785                    | 5     |
| 0.5220     | 0.9821         | 0.9969               | 1.6444          | 0.5845              | 0.7922                    | 6     |
| 0.3104     | 0.9956         | 0.9981               | 1.6041          | 0.5770              | 0.8035                    | 7     |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
