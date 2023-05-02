---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
model-index:
- name: bert-base-uncased-finetuned-ner-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-ner-finetuned-ner

This model is a fine-tuned version of [EffyLi/bert-base-uncased-finetuned-ner](https://huggingface.co/EffyLi/bert-base-uncased-finetuned-ner) on the conll2003 dataset.

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Framework versions

- Transformers 4.18.0
- Pytorch 1.12.0
- Datasets 2.7.1
- Tokenizers 0.11.0
