---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Krishadow/biobert-finetuned-ner-K
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Krishadow/biobert-finetuned-ner-K

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0099
- Validation Loss: 0.0676
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 1695, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.1222     | 0.0604          | 0     |
| 0.0398     | 0.0531          | 1     |
| 0.0220     | 0.0616          | 2     |
| 0.0134     | 0.0653          | 3     |
| 0.0099     | 0.0676          | 4     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.8.0
- Datasets 2.1.0
- Tokenizers 0.12.1
