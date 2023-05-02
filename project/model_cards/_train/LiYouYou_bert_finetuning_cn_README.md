---
language:
- en
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: bert_finetuning_cn
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE SST2
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8314220183486238
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert_finetuning_cn

This model is a fine-tuned version of [bert-base-chinese](https://huggingface.co/bert-base-chinese) on the GLUE SST2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5440
- Accuracy: 0.8314

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results



### Framework versions

- Transformers 4.19.0.dev0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
