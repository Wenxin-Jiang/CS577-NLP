---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: EdBianchi/T5-finetuned-abstracts
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# EdBianchi/T5-finetuned-abstracts

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.9469
- Train Lr: 0.0004
- Validation Loss: 1.8462
- Validation Lr: 0.0002
- Epoch: 1

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 0.00015378147, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Lr | Validation Loss | Validation Lr | Epoch |
|:----------:|:--------:|:---------------:|:-------------:|:-----:|
| 2.2534     | 0.0005   | 1.9839          | 0.0007        | 0     |
| 1.9469     | 0.0004   | 1.8462          | 0.0002        | 1     |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.10.0
- Datasets 2.4.0
- Tokenizers 0.12.1
