---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- source_data_nlp
metrics:
- precision
- recall
- f1
model-index:
- name: sd-smallmol-roles-v2
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: source_data_nlp
      type: source_data_nlp
      args: SMALL_MOL_ROLES
    metrics:
    - name: Precision
      type: precision
      value: 0.9628394473558838
    - name: Recall
      type: recall
      value: 0.9716346153846154
    - name: F1
      type: f1
      value: 0.9672170375687963
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sd-smallmol-roles-v2

This model is a fine-tuned version of [michiyasunaga/BioLinkBERT-large](https://huggingface.co/michiyasunaga/BioLinkBERT-large) on the source_data_nlp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0015
- Accuracy Score: 0.9995
- Precision: 0.9628
- Recall: 0.9716
- F1: 0.9672

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 256
- seed: 42
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy Score | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:---------:|:------:|:------:|
| 0.0013        | 1.0   | 1569 | 0.0015          | 0.9995         | 0.9628    | 0.9716 | 0.9672 |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0a0+bfe5ad2
- Datasets 1.17.0
- Tokenizers 0.12.1
