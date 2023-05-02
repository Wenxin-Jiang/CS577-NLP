---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: DLL888/bert-base-uncased-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# DLL888/bert-base-uncased-squad

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on [SQuAD](https://huggingface.co/datasets/squad) dataset.
It achieves the following results on the evaluation set:
- Exact Match: 80.21759697256385
- F1: 87.77849998885436

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training Machine

Trained in Google Colab Pro with the following specs:

- A100-SXM4-40GB
- NVIDIA-SMI 460.32.03
- Driver Version: 460.32.03
- CUDA Version: 11.2

Training took about 26 minutes for two epochs.

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 2e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 10564, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 500, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: mixed_float16

### Training results

| Train Loss | Train End Logits Accuracy | Train Start Logits Accuracy | Validation Loss | Validation End Logits Accuracy | Validation Start Logits Accuracy | Epoch |
|:----------:|:-------------------------:|:---------------------------:|:---------------:|:------------------------------:|:--------------------------------:|:-----:|
| 1.4348     | 0.6368                    | 0.5974                      | 1.0155          | 0.7193                         | 0.6825                           | 0     |
| 0.8072     | 0.7735                    | 0.7320                      | 0.9990          | 0.7302                         | 0.6983                           | 1     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.7.1
- Tokenizers 0.13.2
