---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Rocketknight1/distilbert-base-uncased-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Rocketknight1/distilbert-base-uncased-finetuned-squad

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.5124
- Train End Logits Accuracy: 0.6041
- Train Start Logits Accuracy: 0.5680
- Validation Loss: 1.1534
- Validation End Logits Accuracy: 0.6849
- Validation Start Logits Accuracy: 0.6443
- Epoch: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 11064, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train End Logits Accuracy | Train Start Logits Accuracy | Validation Loss | Validation End Logits Accuracy | Validation Start Logits Accuracy | Epoch |
|:----------:|:-------------------------:|:---------------------------:|:---------------:|:------------------------------:|:--------------------------------:|:-----:|
| 1.5124     | 0.6041                    | 0.5680                      | 1.1534          | 0.6849                         | 0.6443                           | 0     |


### Framework versions

- Transformers 4.21.0.dev0
- TensorFlow 2.9.1
- Datasets 2.3.3.dev0
- Tokenizers 0.11.0
