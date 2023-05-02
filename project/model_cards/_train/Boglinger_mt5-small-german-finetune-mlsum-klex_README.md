---
tags:
- generated_from_keras_callback
model-index:
- name: Boglinger/mt5-small-german-finetune-mlsum-klex
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Boglinger/mt5-small-german-finetune-mlsum-klex

This model is a fine-tuned version of [ml6team/mt5-small-german-finetune-mlsum](https://huggingface.co/ml6team/mt5-small-german-finetune-mlsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.7473
- Validation Loss: 3.3362
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 744, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 4.1761     | 3.5532          | 0     |
| 3.9847     | 3.4679          | 1     |
| 3.9027     | 3.4180          | 2     |
| 3.8483     | 3.3838          | 3     |
| 3.8075     | 3.3593          | 4     |
| 3.7779     | 3.3476          | 5     |
| 3.7570     | 3.3393          | 6     |
| 3.7446     | 3.3362          | 7     |
| 3.7506     | 3.3362          | 8     |
| 3.7473     | 3.3362          | 9     |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1
