---
tags:
- generated_from_keras_callback
model-index:
- name: ru_propaganda_model_with_foreign_agent_mask
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# ru_propaganda_model_with_foreign_agent_mask

This model is a fine-tuned version of [DeepPavlov/bert-base-bg-cs-pl-ru-cased](https://huggingface.co/DeepPavlov/bert-base-bg-cs-pl-ru-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0659
- Validation Loss: 0.3494
- Train Accuracy: 0.9
- Epoch: 4

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 370, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Accuracy | Epoch |
|:----------:|:---------------:|:--------------:|:-----:|
| 0.6139     | 0.3611          | 0.86           | 0     |
| 0.2522     | 0.3060          | 0.86           | 1     |
| 0.1836     | 0.2757          | 0.92           | 2     |
| 0.1020     | 0.3094          | 0.92           | 3     |
| 0.0659     | 0.3494          | 0.9            | 4     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.2
- Datasets 2.8.0
- Tokenizers 0.13.2
