---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-224-wi2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-224-wi2

This model is a fine-tuned version of [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.3098
- Train Accuracy: 0.9821
- Train Top-5-accuracy: 0.9971
- Validation Loss: 3.0737
- Validation Accuracy: 0.2491
- Validation Top-5-accuracy: 0.4476
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 0.0003, 'decay_steps': 1750, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.001}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-5-accuracy | Validation Loss | Validation Accuracy | Validation Top-5-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 4.4859     | 0.0195         | 0.0579               | 4.2995          | 0.0368              | 0.0865                    | 0     |
| 4.1729     | 0.0355         | 0.0987               | 4.0916          | 0.0472              | 0.1266                    | 1     |
| 3.9541     | 0.0666         | 0.1641               | 3.8050          | 0.0781              | 0.2035                    | 2     |
| 3.5823     | 0.1247         | 0.2615               | 3.4015          | 0.1429              | 0.2950                    | 3     |
| 3.0156     | 0.1913         | 0.3987               | 3.0598          | 0.1880              | 0.3916                    | 4     |
| 2.4618     | 0.3077         | 0.5572               | 2.9869          | 0.2056              | 0.4129                    | 5     |
| 1.8979     | 0.4541         | 0.7165               | 2.9507          | 0.2298              | 0.4425                    | 6     |
| 1.2075     | 0.6914         | 0.8886               | 3.0106          | 0.2394              | 0.4425                    | 7     |
| 0.6026     | 0.9097         | 0.9810               | 3.0739          | 0.2428              | 0.4413                    | 8     |
| 0.3098     | 0.9821         | 0.9971               | 3.0737          | 0.2491              | 0.4476                    | 9     |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
