---
tags:
- generated_from_keras_callback
model-index:
- name: afrodp95/bert-base-spanish-wwm-cased-finetuned-job-skills-ner
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# afrodp95/bert-base-spanish-wwm-cased-finetuned-job-skills-ner

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0894
- Validation Loss: 0.1205
- Train Precision: 0.4356
- Train Recall: 0.5321
- Train F1: 0.4790
- Train Accuracy: 0.9561
- Epoch: 3

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 924, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Precision | Train Recall | Train F1 | Train Accuracy | Epoch |
|:----------:|:---------------:|:---------------:|:------------:|:--------:|:--------------:|:-----:|
| 0.2975     | 0.1545          | 0.3661          | 0.3194       | 0.3411   | 0.9547         | 0     |
| 0.1355     | 0.1216          | 0.4282          | 0.4544       | 0.4409   | 0.9584         | 1     |
| 0.1055     | 0.1189          | 0.4506          | 0.5431       | 0.4925   | 0.9572         | 2     |
| 0.0894     | 0.1205          | 0.4356          | 0.5321       | 0.4790   | 0.9561         | 3     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.2
