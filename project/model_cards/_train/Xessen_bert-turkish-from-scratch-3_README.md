---
tags:
- generated_from_keras_callback
model-index:
- name: bert-turkish-from-scratch-3
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# bert-turkish-from-scratch-3

This model is a fine-tuned version of [](https://huggingface.co/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1112
- Train Accuracy: 0.9853
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
- optimizer: {'name': 'LAMB', 'learning_rate': 0.001, 'weight_decay': 0.0, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-06, 'exclude_from_weight_decay': None, 'exclude_from_layer_adaptation': None}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Epoch |
|:----------:|:--------------:|:-----:|
| 0.5533     | 0.9384         | 0     |
| 0.2784     | 0.9611         | 1     |
| 0.1598     | 0.9801         | 2     |
| 0.1423     | 0.9827         | 3     |
| 0.1348     | 0.9838         | 4     |
| 0.1292     | 0.9841         | 5     |
| 0.1238     | 0.9844         | 6     |
| 0.1186     | 0.9848         | 7     |
| 0.1145     | 0.9851         | 8     |
| 0.1112     | 0.9853         | 9     |


### Framework versions

- Transformers 4.26.0.dev0
- TensorFlow 2.12.0-dev20221226
- Datasets 2.8.0
- Tokenizers 0.13.2
