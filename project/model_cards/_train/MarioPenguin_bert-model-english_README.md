---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: bert-model-english
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# bert-model-english

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1408
- Train Sparse Categorical Accuracy: 0.9512
- Validation Loss: nan
- Validation Sparse Categorical Accuracy: 0.0
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
- optimizer: {'name': 'Adam', 'learning_rate': 5e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Sparse Categorical Accuracy | Validation Loss | Validation Sparse Categorical Accuracy | Epoch |
|:----------:|:---------------------------------:|:---------------:|:--------------------------------------:|:-----:|
| 0.2775     | 0.8887                            | nan             | 0.0                                    | 0     |
| 0.1702     | 0.9390                            | nan             | 0.0                                    | 1     |
| 0.1300     | 0.9555                            | nan             | 0.0                                    | 2     |
| 0.1346     | 0.9544                            | nan             | 0.0                                    | 3     |
| 0.1408     | 0.9512                            | nan             | 0.0                                    | 4     |


### Framework versions

- Transformers 4.16.2
- TensorFlow 2.7.0
- Datasets 1.18.3
- Tokenizers 0.11.0
