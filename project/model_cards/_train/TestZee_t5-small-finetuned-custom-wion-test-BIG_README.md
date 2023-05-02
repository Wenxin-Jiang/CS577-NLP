---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: TestZee/t5-small-finetuned-custom-wion-test-BIG
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# TestZee/t5-small-finetuned-custom-wion-test-BIG

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.1165
- Validation Loss: 0.4609
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.9622     | 0.8875          | 0     |
| 1.9276     | 0.8601          | 1     |
| 1.8301     | 0.8342          | 2     |
| 1.7776     | 0.8104          | 3     |
| 1.7345     | 0.7878          | 4     |
| 1.7733     | 0.7660          | 5     |
| 1.5626     | 0.7448          | 6     |
| 1.6111     | 0.7245          | 7     |
| 1.6754     | 0.7050          | 8     |
| 1.5030     | 0.6867          | 9     |
| 1.5101     | 0.6696          | 10    |
| 1.4328     | 0.6536          | 11    |
| 1.4311     | 0.6383          | 12    |
| 1.3917     | 0.6232          | 13    |
| 1.4102     | 0.6071          | 14    |
| 1.3732     | 0.5948          | 15    |
| 1.3468     | 0.5828          | 16    |
| 1.2817     | 0.5712          | 17    |
| 1.2920     | 0.5600          | 18    |
| 1.2696     | 0.5491          | 19    |
| 1.2552     | 0.5385          | 20    |
| 1.1859     | 0.5285          | 21    |
| 1.1995     | 0.5188          | 22    |
| 1.1690     | 0.5094          | 23    |
| 1.1678     | 0.5003          | 24    |
| 1.1420     | 0.4916          | 25    |
| 1.0959     | 0.4830          | 26    |
| 1.0848     | 0.4750          | 27    |
| 1.1248     | 0.4677          | 28    |
| 1.1165     | 0.4609          | 29    |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1
