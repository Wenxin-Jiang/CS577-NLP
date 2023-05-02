---
tags:
- generated_from_keras_callback
model-index:
- name: Ashraf-kasem/gpt2_fine_tune_with_callback_PolynomialDecay_from_local
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Ashraf-kasem/gpt2_fine_tune_with_callback_PolynomialDecay_from_local

This model is a fine-tuned version of [Ashraf-kasem/gpt2_fine_tune_with_callback_PolynomialDecay_from_local](https://huggingface.co/Ashraf-kasem/gpt2_fine_tune_with_callback_PolynomialDecay_from_local) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.4591
- Validation Loss: 4.1433
- Epoch: 49

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 231100, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 2.0567     | 3.4196          | 0     |
| 2.0328     | 3.4604          | 1     |
| 2.0056     | 3.5015          | 2     |
| 1.9789     | 3.5125          | 3     |
| 1.9530     | 3.5556          | 4     |
| 1.9285     | 3.5970          | 5     |
| 1.9051     | 3.6428          | 6     |
| 1.8823     | 3.6087          | 7     |
| 1.8607     | 3.6300          | 8     |
| 1.8402     | 3.6607          | 9     |
| 1.8202     | 3.7323          | 10    |
| 1.8014     | 3.7363          | 11    |
| 1.7832     | 3.7573          | 12    |
| 1.7660     | 3.7414          | 13    |
| 1.7493     | 3.7810          | 14    |
| 1.7330     | 3.8443          | 15    |
| 1.7175     | 3.8305          | 16    |
| 1.7029     | 3.8547          | 17    |
| 1.6887     | 3.8189          | 18    |
| 1.6753     | 3.8725          | 19    |
| 1.6622     | 3.9050          | 20    |
| 1.6498     | 3.9306          | 21    |
| 1.6376     | 3.9670          | 22    |
| 1.6262     | 3.9569          | 23    |
| 1.6150     | 3.9473          | 24    |
| 1.6044     | 3.9695          | 25    |
| 1.5943     | 3.9193          | 26    |
| 1.5844     | 3.9739          | 27    |
| 1.5751     | 4.0273          | 28    |
| 1.5660     | 4.0224          | 29    |
| 1.5574     | 4.0163          | 30    |
| 1.5491     | 4.0466          | 31    |
| 1.5413     | 4.0520          | 32    |
| 1.5342     | 4.0640          | 33    |
| 1.5270     | 4.0616          | 34    |
| 1.5199     | 4.0611          | 35    |
| 1.5133     | 4.0884          | 36    |
| 1.5073     | 4.0827          | 37    |
| 1.5015     | 4.0972          | 38    |
| 1.4962     | 4.0991          | 39    |
| 1.4908     | 4.0989          | 40    |
| 1.4858     | 4.1078          | 41    |
| 1.4814     | 4.1295          | 42    |
| 1.4773     | 4.1142          | 43    |
| 1.4730     | 4.1200          | 44    |
| 1.4699     | 4.1270          | 45    |
| 1.4664     | 4.1425          | 46    |
| 1.4637     | 4.1392          | 47    |
| 1.4612     | 4.1365          | 48    |
| 1.4591     | 4.1433          | 49    |


### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.0
- Datasets 2.8.0
- Tokenizers 0.13.2
