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
model-index:
- name: bert-base-uncased-wnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE WNLI
      type: glue
      args: wnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.5633802816901409
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-wnli

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE WNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6959
- Accuracy: 0.5634

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 20   | 0.6933          | 0.5493   |
| No log        | 2.0   | 40   | 0.6959          | 0.5634   |
| No log        | 3.0   | 60   | 0.6978          | 0.5352   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
