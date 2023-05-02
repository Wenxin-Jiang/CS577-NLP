

---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Tarkan/distilbert-base-uncased-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Tarkan/distilbert-base-uncased-finetuned-ner
SA yakında silicem bunu xd
This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0588
- Validation Loss: 0.0735
- Train Precision: 0.7787
- Train Recall: 0.8428
- Train F1: 0.8095
- Train Accuracy: 0.9780
- Epoch: 1

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 678, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Precision | Train Recall | Train F1 | Train Accuracy | Epoch |
|:----------:|:---------------:|:---------------:|:------------:|:--------:|:--------------:|:-----:|
| 0.1737     | 0.0799          | 0.7422          | 0.8296       | 0.7835   | 0.9746         | 0     |
| 0.0588     | 0.0735          | 0.7787          | 0.8428       | 0.8095   | 0.9780         | 1     |


### Framework versions

- Transformers 4.21.0
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
