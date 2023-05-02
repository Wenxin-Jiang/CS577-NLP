---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Thalesian/SciGPT-2-finetuned-papers
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Thalesian/SciGPT-2-finetuned-papers

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.8928
- Validation Loss: 2.0726
- Epoch: 19

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'clipvalue': 0.7, 'learning_rate': {'class_name': 'ExponentialDecay', 'config': {'initial_learning_rate': 0.0005, 'decay_steps': 500, 'decay_rate': 0.95, 'staircase': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.1}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.8976     | 2.0729          | 0     |
| 1.8954     | 2.0728          | 1     |
| 1.8942     | 2.0725          | 2     |
| 1.8937     | 2.0726          | 3     |
| 1.8932     | 2.0727          | 4     |
| 1.8929     | 2.0727          | 5     |
| 1.8929     | 2.0727          | 6     |
| 1.8926     | 2.0726          | 7     |
| 1.8928     | 2.0726          | 8     |
| 1.8926     | 2.0726          | 9     |
| 1.8927     | 2.0726          | 10    |
| 1.8927     | 2.0726          | 11    |
| 1.8927     | 2.0726          | 12    |
| 1.8926     | 2.0726          | 13    |
| 1.8927     | 2.0726          | 14    |
| 1.8927     | 2.0726          | 15    |
| 1.8927     | 2.0726          | 16    |
| 1.8927     | 2.0726          | 17    |
| 1.8927     | 2.0726          | 18    |
| 1.8928     | 2.0726          | 19    |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.8.0
- Datasets 2.8.0
- Tokenizers 0.13.2
