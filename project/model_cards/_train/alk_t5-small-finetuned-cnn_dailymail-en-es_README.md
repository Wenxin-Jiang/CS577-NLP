---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: alk/t5-small-finetuned-cnn_dailymail-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# alk/t5-small-finetuned-cnn_dailymail-en-es

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.9163
- Validation Loss: 1.7610
- Epoch: 3

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 71776, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.9945     | 1.7837          | 0     |
| 1.9478     | 1.7694          | 1     |
| 1.9278     | 1.7646          | 2     |
| 1.9163     | 1.7610          | 3     |


### Framework versions

- Transformers 4.19.0
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1
