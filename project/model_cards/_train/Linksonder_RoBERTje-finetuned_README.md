---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: Linksonder/RoBERTje-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Linksonder/RoBERTje-finetuned

This model is a fine-tuned version of [DTAI-KULeuven/robbertje-1-gb-shuffled](https://huggingface.co/DTAI-KULeuven/robbertje-1-gb-shuffled) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 16.5695
- Validation Loss: 17.2618
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 2e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': -992, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 1000, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 16.5695    | 17.2618         | 0     |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.5.0
- Datasets 2.4.0
- Tokenizers 0.12.1
