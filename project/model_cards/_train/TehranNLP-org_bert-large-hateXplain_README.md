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
      name: HATEXPLAIN
      type: ''
      args: hatexplain
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.40790842872008326
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SEED0042

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the HATEXPLAIN dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7731
- Accuracy: 0.4079
- Accuracy 0: 0.8027
- Accuracy 1: 0.1869
- Accuracy 2: 0.2956

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
- lr_scheduler_warmup_steps: 150
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Accuracy 0 | Accuracy 1 | Accuracy 2 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:----------:|:----------:|:----------:|
| No log        | 1.0   | 480  | 0.8029          | 0.4235   | 0.7589     | 0.0461     | 0.5985     |
| No log        | 2.0   | 960  | 0.7574          | 0.4011   | 0.7470     | 0.1831     | 0.3376     |
| No log        | 3.0   | 1440 | 0.7731          | 0.4079   | 0.8027     | 0.1869     | 0.2956     |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu113
- Datasets 2.1.0
- Tokenizers 0.11.6
