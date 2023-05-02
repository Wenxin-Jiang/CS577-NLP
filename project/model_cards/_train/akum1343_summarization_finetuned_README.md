---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: summarization_finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# summarization_finetuned

This model is a fine-tuned version of [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.5478
- Validation Loss: 1.4195
- Train Rougel: tf.Tensor(0.29894578, shape=(), dtype=float32)
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
- optimizer: {'name': 'Adamax', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Rougel                                   | Epoch |
|:----------:|:---------------:|:----------------------------------------------:|:-----:|
| 1.5478     | 1.4195          | tf.Tensor(0.29894578, shape=(), dtype=float32) | 0     |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.10.0
- Datasets 2.6.1
- Tokenizers 0.12.1
