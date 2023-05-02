---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: my_Med
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# my_Med

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.5902
- Validation Loss: 1.3655
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 2.8689     | 2.0671          | 0     |
| 2.2250     | 1.8456          | 1     |
| 2.0132     | 1.7104          | 2     |
| 1.9079     | 1.6828          | 3     |
| 1.8237     | 1.5935          | 4     |
| 1.7651     | 1.5240          | 5     |
| 1.7246     | 1.4930          | 6     |
| 1.6565     | 1.4191          | 7     |
| 1.6166     | 1.3944          | 8     |
| 1.5902     | 1.3655          | 9     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.2
- Datasets 2.7.1
- Tokenizers 0.13.2
