---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: opus-mt-ar-en-finetunedTanzil-v7-ar-to-en
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# opus-mt-ar-en-finetunedTanzil-v7-ar-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1919
- Validation Loss: 0.5047
- Train Rouge1: 49.6877
- Train Rouge2: 25.9574
- Train Rougel: 45.2590
- Train Rougelsum: 45.7464
- Train Gen Len: 85.57
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
| 0.1959     | 0.5105          | 48.2182      | 23.4978      | 44.1127      | 44.6422         | 87.45         | 0     |
| 0.1950     | 0.5114          | 49.5777      | 25.1663      | 45.7183      | 46.0930         | 86.72         | 1     |
| 0.1937     | 0.5074          | 49.1793      | 24.1899      | 45.3374      | 45.5902         | 84.805        | 2     |
| 0.1929     | 0.5075          | 49.1553      | 24.8199      | 44.7342      | 45.1392         | 87.495        | 3     |
| 0.1919     | 0.5047          | 49.6877      | 25.9574      | 45.2590      | 45.7464         | 85.57         | 4     |


### Framework versions

- Transformers 4.17.0.dev0
- TensorFlow 2.7.0
- Datasets 1.18.4.dev0
- Tokenizers 0.10.3
