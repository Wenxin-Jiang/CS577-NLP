---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-384-wi4
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-384-wi4

This model is a fine-tuned version of [google/vit-base-patch16-384](https://huggingface.co/google/vit-base-patch16-384) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1742
- Train Accuracy: 0.9982
- Train Top-3-accuracy: 0.9997
- Validation Loss: 1.5010
- Validation Accuracy: 0.5746
- Validation Top-3-accuracy: 0.8040
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 1800, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 3.7777     | 0.0845         | 0.1855               | 3.3754          | 0.1543              | 0.3014                    | 0     |
| 2.7253     | 0.3277         | 0.5560               | 2.4975          | 0.3452              | 0.5892                    | 1     |
| 2.0079     | 0.5236         | 0.7589               | 2.1228          | 0.4234              | 0.6882                    | 2     |
| 1.5256     | 0.6663         | 0.8549               | 1.9117          | 0.4734              | 0.7445                    | 3     |
| 1.1602     | 0.7712         | 0.9270               | 1.8059          | 0.5162              | 0.7560                    | 4     |
| 0.8509     | 0.8659         | 0.9614               | 1.6534          | 0.5516              | 0.7758                    | 5     |
| 0.5955     | 0.9353         | 0.9836               | 1.6139          | 0.5610              | 0.7935                    | 6     |
| 0.4229     | 0.9687         | 0.9940               | 1.5655          | 0.5631              | 0.7925                    | 7     |
| 0.3045     | 0.9859         | 0.9979               | 1.5290          | 0.5714              | 0.7987                    | 8     |
| 0.2221     | 0.9958         | 0.9990               | 1.5061          | 0.5954              | 0.8008                    | 9     |
| 0.1742     | 0.9982         | 0.9997               | 1.5010          | 0.5746              | 0.8040                    | 10    |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
