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
model_index:
- name: rte
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE RTE
      type: glue
      args: rte
    metric:
      name: Accuracy
      type: accuracy
      value: 0.6859205776173285
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# rte

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on the GLUE RTE dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7994
- Accuracy: 0.6859

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4.0

### Training results



### Framework versions

- Transformers 4.9.0
- Pytorch 1.9.0+cu102
- Datasets 1.10.2
- Tokenizers 0.10.3
