---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: DavidNo/albert-xxlarge-v2-finetuned-squadv2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# DavidNo/albert-xxlarge-v2-finetuned-squadv2

This model is a fine-tuned version of [albert-xxlarge-v2](https://huggingface.co/albert-xxlarge-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.7633
- Train End Logits Accuracy: 0.6680
- Train Start Logits Accuracy: 0.6407
- Validation Loss: 1.1441
- Validation End Logits Accuracy: 0.5277
- Validation Start Logits Accuracy: 0.5106
- Epoch: 1

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 16494, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train End Logits Accuracy | Train Start Logits Accuracy | Validation Loss | Validation End Logits Accuracy | Validation Start Logits Accuracy | Epoch |
|:----------:|:-------------------------:|:---------------------------:|:---------------:|:------------------------------:|:--------------------------------:|:-----:|
| 1.0842     | 0.6032                    | 0.5767                      | 1.1372          | 0.5166                         | 0.5058                           | 0     |
| 0.7633     | 0.6680                    | 0.6407                      | 1.1441          | 0.5277                         | 0.5106                           | 1     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.2
