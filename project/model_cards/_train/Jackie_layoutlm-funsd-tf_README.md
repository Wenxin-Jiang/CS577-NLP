---
tags:
- generated_from_keras_callback
model-index:
- name: layoutlm-funsd-tf
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# layoutlm-funsd-tf

This model is a fine-tuned version of [microsoft/layoutlm-base-uncased](https://huggingface.co/microsoft/layoutlm-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.2477
- Validation Loss: 0.7106
- Train Overall Precision: 0.7360
- Train Overall Recall: 0.7918
- Train Overall F1: 0.7629
- Train Overall Accuracy: 0.7983
- Epoch: 7

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 3e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Train Overall Precision | Train Overall Recall | Train Overall F1 | Train Overall Accuracy | Epoch |
|:----------:|:---------------:|:-----------------------:|:--------------------:|:----------------:|:----------------------:|:-----:|
| 1.7300     | 1.4338          | 0.1989                  | 0.2313               | 0.2139           | 0.5265                 | 0     |
| 1.1984     | 0.8999          | 0.5775                  | 0.5795               | 0.5785           | 0.7162                 | 1     |
| 0.7785     | 0.7393          | 0.6713                  | 0.7040               | 0.6872           | 0.7634                 | 2     |
| 0.5666     | 0.6416          | 0.7113                  | 0.7617               | 0.7356           | 0.7961                 | 3     |
| 0.4447     | 0.6454          | 0.7165                  | 0.7737               | 0.7440           | 0.8003                 | 4     |
| 0.3647     | 0.6500          | 0.7353                  | 0.7832               | 0.7585           | 0.8091                 | 5     |
| 0.3044     | 0.6587          | 0.7266                  | 0.8053               | 0.7639           | 0.8119                 | 6     |
| 0.2477     | 0.7106          | 0.7360                  | 0.7918               | 0.7629           | 0.7983                 | 7     |


### Framework versions

- Transformers 4.23.1
- TensorFlow 2.9.2
- Datasets 2.6.0
- Tokenizers 0.13.1
