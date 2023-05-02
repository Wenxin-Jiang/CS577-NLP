---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: Ashraf-kasem/custom_gpt2_frames_text
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Ashraf-kasem/custom_gpt2_frames_text

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.3938
- Validation Loss: 2.0834
- Epoch: 29

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 188670, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 5.4252     | 4.4731          | 0     |
| 4.1781     | 3.6928          | 1     |
| 3.5744     | 3.2572          | 2     |
| 3.1856     | 2.9789          | 3     |
| 2.9095     | 2.7887          | 4     |
| 2.6999     | 2.6534          | 5     |
| 2.5334     | 2.5484          | 6     |
| 2.3969     | 2.4706          | 7     |
| 2.2826     | 2.4102          | 8     |
| 2.1842     | 2.3518          | 9     |
| 2.0988     | 2.3096          | 10    |
| 2.0236     | 2.2740          | 11    |
| 1.9569     | 2.2443          | 12    |
| 1.8960     | 2.2214          | 13    |
| 1.8411     | 2.1954          | 14    |
| 1.7913     | 2.1815          | 15    |
| 1.7457     | 2.1652          | 16    |
| 1.7034     | 2.1552          | 17    |
| 1.6648     | 2.1398          | 18    |
| 1.6288     | 2.1289          | 19    |
| 1.5955     | 2.1213          | 20    |
| 1.5643     | 2.1114          | 21    |
| 1.5359     | 2.1071          | 22    |
| 1.5094     | 2.0998          | 23    |
| 1.4846     | 2.0942          | 24    |
| 1.4622     | 2.0911          | 25    |
| 1.4420     | 2.0893          | 26    |
| 1.4233     | 2.0879          | 27    |
| 1.4074     | 2.0838          | 28    |
| 1.3938     | 2.0834          | 29    |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.0
- Datasets 2.8.0
- Tokenizers 0.13.2
