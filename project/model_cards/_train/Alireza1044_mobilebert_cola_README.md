---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: cola
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE COLA
      type: glue
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.5277813760438573
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# cola

This model is a fine-tuned version of [google/mobilebert-uncased](https://huggingface.co/google/mobilebert-uncased) on the GLUE COLA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6337
- Matthews Correlation: 0.5278

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results



### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1
