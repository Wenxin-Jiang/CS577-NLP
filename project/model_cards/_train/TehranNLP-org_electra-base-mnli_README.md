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
      value: 0.8879266428935303
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SEED0042

This model is a fine-tuned version of [google/electra-base-discriminator](https://huggingface.co/google/electra-base-discriminator) on the MNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4265
- Accuracy: 0.8879

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
- distributed_type: not_parallel
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.3762        | 1.0   | 12272 | 0.3312          | 0.8794   |
| 0.2542        | 2.0   | 24544 | 0.3467          | 0.8843   |
| 0.1503        | 3.0   | 36816 | 0.4265          | 0.8879   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu113
- Datasets 2.1.0
- Tokenizers 0.11.6
