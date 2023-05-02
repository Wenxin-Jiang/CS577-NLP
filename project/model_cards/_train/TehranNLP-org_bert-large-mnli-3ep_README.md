---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: SEED0042
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: MNLI
      type: ''
      args: mnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8572592969943963
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SEED0042

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the MNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5092
- Accuracy: 0.8573

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: not_parallel
- gradient_accumulation_steps: 32
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.4736        | 1.0   | 12271 | 0.4213          | 0.8372   |
| 0.3248        | 2.0   | 24542 | 0.4055          | 0.8538   |
| 0.1571        | 3.0   | 36813 | 0.5092          | 0.8573   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu113
- Datasets 2.1.0
- Tokenizers 0.11.6
