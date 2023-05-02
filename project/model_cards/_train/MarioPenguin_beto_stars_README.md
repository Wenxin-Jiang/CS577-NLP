---
tags:
- generated_from_keras_callback
model-index:
- name: beto_stars
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# beto_stars

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-uncased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.8954
- Train Accuracy: 0.6248
- Validation Loss: 1.1278
- Validation Accuracy: 0.5148
- Epoch: 14

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 5e-07, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 1.5935     | 0.2626         | 1.5553          | 0.3482              | 0     |
| 1.5072     | 0.3782         | 1.4289          | 0.4188              | 1     |
| 1.3590     | 0.4312         | 1.2929          | 0.4406              | 2     |
| 1.2463     | 0.4628         | 1.2197          | 0.4682              | 3     |
| 1.1754     | 0.4970         | 1.1785          | 0.4830              | 4     |
| 1.1299     | 0.5114         | 1.1533          | 0.4908              | 5     |
| 1.0847     | 0.5362         | 1.1398          | 0.5006              | 6     |
| 1.0492     | 0.5440         | 1.1273          | 0.5046              | 7     |
| 1.0278     | 0.5592         | 1.1237          | 0.5034              | 8     |
| 1.0031     | 0.5690         | 1.1171          | 0.5118              | 9     |
| 0.9798     | 0.5712         | 1.1163          | 0.5120              | 10    |
| 0.9598     | 0.5894         | 1.1180          | 0.5114              | 11    |
| 0.9406     | 0.5964         | 1.1219          | 0.5122              | 12    |
| 0.9178     | 0.6104         | 1.1269          | 0.5150              | 13    |
| 0.8954     | 0.6248         | 1.1278          | 0.5148              | 14    |


### Framework versions

- Transformers 4.17.0
- TensorFlow 2.8.0
- Datasets 1.18.4
- Tokenizers 0.11.6
