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
- name: sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE SST2
      type: glue
      args: sst2
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9231651376146789
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sst2

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on the GLUE SST2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3808
- Accuracy: 0.9232

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
