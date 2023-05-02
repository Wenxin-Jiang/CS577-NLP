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
- name: mrpc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE MRPC
      type: glue
      args: mrpc
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8382352941176471
    - name: F1
      type: f1
      value: 0.8888888888888888
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mrpc

This model is a fine-tuned version of [google/mobilebert-uncased](https://huggingface.co/google/mobilebert-uncased) on the GLUE MRPC dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3672
- Accuracy: 0.8382
- F1: 0.8889
- Combined Score: 0.8636

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4.0

### Training results



### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1
