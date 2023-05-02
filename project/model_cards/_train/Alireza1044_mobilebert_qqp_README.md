---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: qqp
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE QQP
      type: glue
      args: qqp
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8988869651249073
    - name: F1
      type: f1
      value: 0.8670050100852366
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# qqp

This model is a fine-tuned version of [google/mobilebert-uncased](https://huggingface.co/google/mobilebert-uncased) on the GLUE QQP dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2458
- Accuracy: 0.8989
- F1: 0.8670
- Combined Score: 0.8829

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
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2.5

### Training results



### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1
