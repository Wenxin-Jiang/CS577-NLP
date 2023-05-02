---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-large-unlabeled-labeled-gab-reddit-task-semeval2023-t10-150000sample
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-unlabeled-labeled-gab-reddit-task-semeval2023-t10-150000sample

This model is a fine-tuned version of [HPL/roberta-large-unlabeled-labeled-gab-reddit-task-semeval2023-t10-90000sample](https://huggingface.co/HPL/roberta-large-unlabeled-labeled-gab-reddit-task-semeval2023-t10-90000sample) on the None dataset.

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results



### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.10.3
