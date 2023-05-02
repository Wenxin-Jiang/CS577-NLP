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
- name: sd-panelization-v2
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: source_data_nlp
      type: source_data_nlp
      args: PANELIZATION
    metrics:
    - name: Precision
      type: precision
      value: 0.9134245120169964
    - name: Recall
      type: recall
      value: 0.9494824016563147
    - name: F1
      type: f1
      value: 0.9311044937736871
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sd-panelization-v2

This model is a fine-tuned version of [michiyasunaga/BioLinkBERT-large](https://huggingface.co/michiyasunaga/BioLinkBERT-large) on the source_data_nlp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0050
- Accuracy Score: 0.9982
- Precision: 0.9134
- Recall: 0.9495
- F1: 0.9311

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
| 0.0048        | 1.0   | 431  | 0.0050          | 0.9982         | 0.9134    | 0.9495 | 0.9311 |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0a0+bfe5ad2
- Datasets 1.17.0
- Tokenizers 0.12.1
