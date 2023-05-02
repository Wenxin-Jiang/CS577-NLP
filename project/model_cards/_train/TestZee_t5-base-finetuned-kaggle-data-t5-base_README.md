---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: TestZee/t5-base-finetuned-kaggle-data-t5-base
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# TestZee/t5-base-finetuned-kaggle-data-t5-base

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.2080
- Validation Loss: 2.0110
- Train Rouge1: 24.3681
- Train Rouge2: 8.7734
- Train Rougel: 18.7763
- Train Rougelsum: 21.1159
- Train Gen Len: 19.0
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 1e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.001}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Train Gen Len | Epoch |
|:----------:|:---------------:|:------------:|:------------:|:------------:|:---------------:|:-------------:|:-----:|
| 2.2080     | 2.0110          | 24.3681      | 8.7734       | 18.7763      | 21.1159         | 19.0          | 0     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.7.1
- Tokenizers 0.13.2
