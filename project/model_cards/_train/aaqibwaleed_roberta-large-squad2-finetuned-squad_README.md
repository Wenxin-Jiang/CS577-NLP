---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: aaqibwaleed/roberta-large-squad2-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# aaqibwaleed/roberta-large-squad2-finetuned-squad

This model is a fine-tuned version of [navteca/roberta-large-squad2](https://huggingface.co/navteca/roberta-large-squad2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.5015
- Train End Logits Accuracy: 0.8536
- Train Start Logits Accuracy: 0.8279
- Validation Loss: 0.7790
- Validation End Logits Accuracy: 0.7905
- Validation Start Logits Accuracy: 0.7799
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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 131822, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train End Logits Accuracy | Train Start Logits Accuracy | Validation Loss | Validation End Logits Accuracy | Validation Start Logits Accuracy | Epoch |
|:----------:|:-------------------------:|:---------------------------:|:---------------:|:------------------------------:|:--------------------------------:|:-----:|
| 0.9483     | 0.7418                    | 0.7176                      | 0.8067          | 0.7573                         | 0.7504                           | 0     |
| 0.5015     | 0.8536                    | 0.8279                      | 0.7790          | 0.7905                         | 0.7799                           | 1     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.7.1
- Datasets 2.7.1
- Tokenizers 0.13.2
