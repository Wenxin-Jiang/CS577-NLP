---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: DLL888/deberta-v3-base-squad
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# DLL888/deberta-v3-base-squad

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the [SQuAD](https://huggingface.co/datasets/squad) dataset.

It achieves the following results on the evaluation set:

- Exact Match: 88.08893093661305
- F1: 93.75543944888847

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
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 2e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 10538, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 500, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train End Logits Accuracy | Train Start Logits Accuracy | Validation Loss | Validation End Logits Accuracy | Validation Start Logits Accuracy | Epoch |
|:----------:|:-------------------------:|:---------------------------:|:---------------:|:------------------------------:|:--------------------------------:|:-----:|
| 1.0540     | 0.7261                    | 0.6885                      | 0.7617          | 0.7841                         | 0.7530                           | 0     |
| 0.6248     | 0.8212                    | 0.7777                      | 0.7594          | 0.7873                         | 0.7569                           | 1     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.7.1
- Tokenizers 0.13.2
