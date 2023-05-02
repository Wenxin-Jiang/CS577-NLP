---
license: apache-2.0
tags:
- generated_from_trainer
model_index:
- name: bert-fa-QA-v1
  results:
  - task:
      name: Question Answering
      type: question-answering
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-fa-QA-v1
Persian Question and answer Model Based on Bert Model

This model is a fine-tuned version of [ParsBERT](https://arxiv.org/abs/2005.12515) on PersianQA dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7297

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.2563        | 1.0   | 1126 | 1.7222          |
| 1.3372        | 2.0   | 2252 | 1.7297          |


### Framework versions

- Transformers 4.9.0
- Pytorch 1.9.0+cu102
- Tokenizers 0.10.3
