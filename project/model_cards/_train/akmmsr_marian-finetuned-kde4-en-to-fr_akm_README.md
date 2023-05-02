---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: akmmsr/marian-finetuned-kde4-en-to-fr_akm
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# akmmsr/marian-finetuned-kde4-en-to-fr_akm

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-fr](https://huggingface.co/Helsinki-NLP/opus-mt-en-fr) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.6861
- Validation Loss: 0.8049
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 17736, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.0625     | 0.8779          | 0     |
| 0.7985     | 0.8221          | 1     |
| 0.6861     | 0.8049          | 2     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.7.1
- Tokenizers 0.13.2
