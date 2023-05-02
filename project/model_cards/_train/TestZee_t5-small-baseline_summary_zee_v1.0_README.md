---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: TestZee/t5-small-baseline_summary_zee_v1.0
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# TestZee/t5-small-baseline_summary_zee_v1.0

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.3722
- Validation Loss: 2.1596
- Train Rouge1: 21.6350
- Train Rouge2: 8.9453
- Train Rougel: 17.8649
- Train Rougelsum: 19.9099
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Train Gen Len | Epoch |
|:----------:|:---------------:|:------------:|:------------:|:------------:|:---------------:|:-------------:|:-----:|
| 2.3722     | 2.1596          | 21.6350      | 8.9453       | 17.8649      | 19.9099         | 19.0          | 0     |


### Framework versions

- Transformers 4.23.1
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.1
