---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: alk/mt5-small-mt5-small-finetuned-billsum-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# alk/mt5-small-mt5-small-finetuned-billsum-en-es

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.1897
- Validation Loss: 1.0147
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 18944, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 4.3673     | 1.7982          | 0     |
| 2.2571     | 1.4674          | 1     |
| 1.8047     | 1.2942          | 2     |
| 1.5579     | 1.1585          | 3     |
| 1.3863     | 1.0762          | 4     |
| 1.2786     | 1.0284          | 5     |
| 1.2162     | 1.0217          | 6     |
| 1.1897     | 1.0147          | 7     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1
