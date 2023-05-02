---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: roberta-model-english
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# roberta-model-english

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1140
- Train Accuracy: 0.9596
- Validation Loss: 0.2166
- Validation Accuracy: 0.9301
- Epoch: 2

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 5e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.2922     | 0.8804         | 0.2054          | 0.9162              | 0     |
| 0.1710     | 0.9352         | 0.1879          | 0.9353              | 1     |
| 0.1140     | 0.9596         | 0.2166          | 0.9301              | 2     |


### Framework versions

- Transformers 4.16.2
- TensorFlow 2.7.0
- Tokenizers 0.11.0
