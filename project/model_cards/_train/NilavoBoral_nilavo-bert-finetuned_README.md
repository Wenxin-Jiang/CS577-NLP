---
tags:
- generated_from_keras_callback
model-index:
- name: NilavoBoral/nilavo-bert-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# NilavoBoral/nilavo-bert-finetuned

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0018
- Validation Loss: 0.0755
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 8780, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.0171     | 0.0676          | 0     |
| 0.0105     | 0.0640          | 1     |
| 0.0058     | 0.0691          | 2     |
| 0.0031     | 0.0733          | 3     |
| 0.0018     | 0.0755          | 4     |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1
