---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Yah216/DistilBERT-finetuned-ACDP
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Yah216/DistilBERT-finetuned-ACDP

This model is a fine-tuned version of [CAMeL-Lab/bert-base-arabic-camelbert-ca](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-ca) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 6.6178
- Validation Loss: 6.2483
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 2e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': -688, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 1000, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 8.7636     | 7.6558          | 0     |
| 7.2645     | 6.7607          | 1     |
| 6.6178     | 6.2483          | 2     |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.2
- Tokenizers 0.12.1
