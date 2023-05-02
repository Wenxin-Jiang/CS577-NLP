---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Metformin/BART_medFineTune
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Metformin/BART_medFineTune

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.7982
- Validation Loss: 0.9953
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 1e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 1e-05, 'decay_steps': 7820, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 100, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 2.1563     | 1.3468          | 0     |
| 1.4157     | 1.2090          | 1     |
| 1.2579     | 1.1387          | 2     |
| 1.1819     | 1.0888          | 3     |
| 1.1438     | 1.0848          | 4     |
| 1.0629     | 1.0512          | 5     |
| 1.0163     | 1.0454          | 6     |
| 0.9801     | 1.0248          | 7     |
| 0.9530     | 1.0171          | 8     |
| 0.9262     | 1.0108          | 9     |
| 0.9124     | 1.0116          | 10    |
| 0.8853     | 1.0043          | 11    |
| 0.8658     | 1.0023          | 12    |
| 0.8511     | 0.9987          | 13    |
| 0.8394     | 0.9988          | 14    |
| 0.8298     | 0.9994          | 15    |
| 0.8175     | 0.9985          | 16    |
| 0.8105     | 0.9936          | 17    |
| 0.8033     | 0.9974          | 18    |
| 0.8012     | 0.9948          | 19    |
| 0.7997     | 0.9948          | 20    |
| 0.7970     | 0.9957          | 21    |
| 0.7956     | 0.9958          | 22    |
| 0.8002     | 0.9954          | 23    |
| 0.7951     | 0.9957          | 24    |
| 0.7994     | 0.9948          | 25    |
| 0.7964     | 0.9958          | 26    |
| 0.7948     | 0.9957          | 27    |
| 0.7979     | 0.9956          | 28    |
| 0.7982     | 0.9953          | 29    |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.6.3
- Datasets 2.0.0
- Tokenizers 0.12.1
