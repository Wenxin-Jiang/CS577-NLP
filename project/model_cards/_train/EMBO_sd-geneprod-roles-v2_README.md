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
- name: sd-geneprod-roles-v2
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: source_data_nlp
      type: source_data_nlp
      args: GENEPROD_ROLES
    metrics:
    - name: Precision
      type: precision
      value: 0.9227577212638568
    - name: Recall
      type: recall
      value: 0.9288143683990692
    - name: F1
      type: f1
      value: 0.9257761389318425
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sd-geneprod-roles-v2

This model is a fine-tuned version of [michiyasunaga/BioLinkBERT-large](https://huggingface.co/michiyasunaga/BioLinkBERT-large) on the source_data_nlp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0136
- Accuracy Score: 0.9950
- Precision: 0.9228
- Recall: 0.9288
- F1: 0.9258

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
| 0.014         | 1.0   | 1569 | 0.0136          | 0.9950         | 0.9228    | 0.9288 | 0.9258 |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0a0+bfe5ad2
- Datasets 1.17.0
- Tokenizers 0.12.1
