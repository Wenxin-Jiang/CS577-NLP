---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad
model_index:
- name: distilbert-base-uncased-finetuned-squad
  results:
  - task:
      name: Question Answering
      type: question-answering
    dataset:
      name: squad
      type: squad
      args: plain_text
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-squad

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the squad dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1520

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.2177        | 1.0   | 5533  | 1.1565          |
| 0.9472        | 2.0   | 11066 | 1.1174          |
| 0.7634        | 3.0   | 16599 | 1.1520          |


### Framework versions

- Transformers 4.9.1
- Pytorch 1.9.0+cu102
- Datasets 1.10.2
- Tokenizers 0.10.3
