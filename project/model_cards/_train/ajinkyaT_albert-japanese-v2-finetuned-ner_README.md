---
tags:
- generated_from_keras_callback
model-index:
- name: ajinkyaT/albert-japanese-v2-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# ajinkyaT/albert-japanese-v2-finetuned-ner

This model is a fine-tuned version of [ajinkyaT/albert-japanese-v2-finetuned-ner](https://huggingface.co/ajinkyaT/albert-japanese-v2-finetuned-ner) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1292
- Validation Loss: 0.1499
- Train Precision: 0.6817
- Train Recall: 0.6951
- Train F1: 0.6883
- Train Accuracy: 0.9594
- Epoch: 9

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 1320, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Precision | Train Recall | Train F1 | Train Accuracy | Epoch |
|:----------:|:---------------:|:---------------:|:------------:|:--------:|:--------------:|:-----:|
| 0.1299     | 0.1499          | 0.6817          | 0.6951       | 0.6883   | 0.9594         | 4     |
| 0.1306     | 0.1499          | 0.6817          | 0.6951       | 0.6883   | 0.9594         | 5     |
| 0.1296     | 0.1499          | 0.6817          | 0.6951       | 0.6883   | 0.9594         | 6     |
| 0.1292     | 0.1499          | 0.6817          | 0.6951       | 0.6883   | 0.9594         | 7     |
| 0.1306     | 0.1499          | 0.6817          | 0.6951       | 0.6883   | 0.9594         | 8     |
| 0.1292     | 0.1499          | 0.6817          | 0.6951       | 0.6883   | 0.9594         | 9     |


### Framework versions

- Transformers 4.23.1
- TensorFlow 2.8.2
- Datasets 2.5.2
- Tokenizers 0.13.1
