---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BERT_MC_OpenBookQA
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_MC_OpenBookQA

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8077
- Accuracy: 0.654

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.8972        | 1.61  | 500  | 0.9912          | 0.636    |
| 0.2906        | 3.23  | 1000 | 1.4448          | 0.654    |
| 0.07          | 4.84  | 1500 | 1.8077          | 0.654    |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.11.0
