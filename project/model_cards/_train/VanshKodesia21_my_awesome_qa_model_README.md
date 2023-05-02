---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: my_awesome_qa_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_qa_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 4.8937

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
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 15   | 4.5857          |
| No log        | 2.0   | 30   | 4.6562          |
| No log        | 3.0   | 45   | 4.8485          |
| No log        | 4.0   | 60   | 4.9157          |
| No log        | 5.0   | 75   | 4.8937          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Tokenizers 0.13.2
