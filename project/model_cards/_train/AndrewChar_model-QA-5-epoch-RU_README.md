---
tags:
- generated_from_keras_callback
language: ru
datasets:
 - sberquad
model-index:
- name: model-QA-5-epoch-RU
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# model-QA-5-epoch-RU

This model is a fine-tuned version of [AndrewChar/diplom-prod-epoch-4-datast-sber-QA](https://huggingface.co/AndrewChar/diplom-prod-epoch-4-datast-sber-QA) on  sberquad
 dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.1991
- Validation Loss: 0.0
- Epoch: 5

## Model description

Модель отвечающая на вопрос по контектсу
 это дипломная работа 
## Intended uses & limitations

Контекст должен содержать не более 512 токенов  

## Training and evaluation data
DataSet SberSQuAD
{'exact_match': 54.586, 'f1': 73.644}

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_re': 2e-06 'decay_steps': 2986, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.1991     |                 | 5     |


### Framework versions

- Transformers 4.15.0
- TensorFlow 2.7.0
- Datasets 1.17.0
- Tokenizers 0.10.3
