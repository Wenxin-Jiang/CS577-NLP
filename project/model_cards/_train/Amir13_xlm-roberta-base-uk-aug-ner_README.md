---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-base-uk-aug-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-uk-aug-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2396
- Precision: 0.6410
- Recall: 0.6370
- F1: 0.6390
- Accuracy: 0.9313

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.6689        | 1.0   | 725  | 0.3466          | 0.4923    | 0.4758 | 0.4839 | 0.9054   |
| 0.3286        | 2.0   | 1450 | 0.2742          | 0.5723    | 0.5894 | 0.5807 | 0.9179   |
| 0.2224        | 3.0   | 2175 | 0.2534          | 0.5884    | 0.6247 | 0.6060 | 0.9240   |
| 0.2008        | 4.0   | 2900 | 0.2396          | 0.6410    | 0.6370 | 0.6390 | 0.9313   |
| 0.1703        | 5.0   | 3625 | 0.2398          | 0.6336    | 0.6476 | 0.6405 | 0.9306   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
