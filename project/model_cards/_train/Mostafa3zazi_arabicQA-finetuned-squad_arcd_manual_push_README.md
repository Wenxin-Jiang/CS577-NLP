---
tags:
- generated_from_keras_callback
model-index:
- name: arabicQA-finetuned-squad_arcd_manual_push
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# arabicQA-finetuned-squad_arcd_manual_push

This model is a fine-tuned version of [aubmindlab/araelectra-base-discriminator](https://huggingface.co/aubmindlab/araelectra-base-discriminator) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.3885
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 3e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 3034, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 50, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Epoch |
|:----------:|:-----:|
| 2.3885     | 0     |


### Framework versions

- Transformers 4.21.1
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
