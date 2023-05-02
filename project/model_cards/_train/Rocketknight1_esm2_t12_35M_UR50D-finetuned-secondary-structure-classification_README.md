---
tags:
- generated_from_keras_callback
model-index:
- name: esm2_t12_35M_UR50D-finetuned-secondary-structure-classification
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# esm2_t12_35M_UR50D-finetuned-secondary-structure-classification

This model is a fine-tuned version of [facebook/esm2_t12_35M_UR50D](https://huggingface.co/facebook/esm2_t12_35M_UR50D) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.4108
- Train Masked Accuracy: 0.8325
- Validation Loss: 0.4586
- Validation Masked Accuracy: 0.8119
- Epoch: 2

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.0}
- training_precision: float32

### Training results

| Train Loss | Train Masked Accuracy | Validation Loss | Validation Masked Accuracy | Epoch |
|:----------:|:---------------------:|:---------------:|:--------------------------:|:-----:|
| 0.5809     | 0.7502                | 0.4764          | 0.8023                     | 0     |
| 0.4534     | 0.8132                | 0.4564          | 0.8115                     | 1     |
| 0.4108     | 0.8325                | 0.4586          | 0.8119                     | 2     |


### Framework versions

- Transformers 4.25.0.dev0
- TensorFlow 2.10.0
- Datasets 2.6.1
- Tokenizers 0.11.0
