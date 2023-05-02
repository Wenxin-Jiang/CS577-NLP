---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: TestZee/t5-small-finetuned-kaggle-data-t5-v2.0
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# TestZee/t5-small-finetuned-kaggle-data-t5-v2.0

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.8648
- Validation Loss: 1.7172
- Train Rouge1: 24.1639
- Train Rouge2: 13.1314
- Train Rougel: 20.8170
- Train Rougelsum: 22.3549
- Train Gen Len: 19.0
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Train Gen Len | Epoch |
|:----------:|:---------------:|:------------:|:------------:|:------------:|:---------------:|:-------------:|:-----:|
| 2.1107     | 1.8251          | 23.3472      | 12.6240      | 20.0726      | 21.6297         | 19.0          | 0     |
| 1.9759     | 1.7755          | 23.8048      | 13.0368      | 20.4876      | 22.1022         | 19.0          | 1     |
| 1.9275     | 1.7466          | 23.9713      | 13.1351      | 20.5833      | 22.1610         | 19.0          | 2     |
| 1.8931     | 1.7291          | 24.0628      | 13.1243      | 20.7427      | 22.2890         | 19.0          | 3     |
| 1.8648     | 1.7172          | 24.1639      | 13.1314      | 20.8170      | 22.3549         | 19.0          | 4     |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1
