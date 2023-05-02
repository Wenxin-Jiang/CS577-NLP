---
tags:
- generated_from_keras_callback
model-index:
- name: beto_amazon_final_pnn
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# beto_amazon_final_pnn

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-uncased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.5242
- Train Accuracy: 0.7838
- Validation Loss: 0.6507
- Validation Accuracy: 0.7284
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
- optimizer: {'name': 'Adam', 'learning_rate': 5e-07, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.6129     | 0.7496         | 0.6588          | 0.7248              | 0     |
| 0.5850     | 0.7566         | 0.6505          | 0.7258              | 1     |
| 0.5604     | 0.7704         | 0.6484          | 0.7278              | 2     |
| 0.5407     | 0.7840         | 0.6503          | 0.7250              | 3     |
| 0.5242     | 0.7838         | 0.6507          | 0.7284              | 4     |


### Framework versions

- Transformers 4.16.2
- TensorFlow 2.8.0
- Datasets 1.18.3
- Tokenizers 0.11.6
