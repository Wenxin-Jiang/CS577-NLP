---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: t5-small-opus_books-en_fr
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# t5-small-opus_books-en_fr

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.7303
- Validation Loss: 1.5141
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.9313     | 1.6143          | 0     |
| 1.7920     | 1.5522          | 1     |
| 1.7303     | 1.5141          | 2     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.7.0
- Tokenizers 0.13.2
