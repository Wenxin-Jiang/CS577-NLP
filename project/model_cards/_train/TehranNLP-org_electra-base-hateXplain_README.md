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
      value: 0.4162330905306972
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SEED0042

This model is a fine-tuned version of [google/electra-base-discriminator](https://huggingface.co/google/electra-base-discriminator) on the HATEXPLAIN dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7667
- Accuracy: 0.4162
- Accuracy 0: 0.8145
- Accuracy 1: 0.1895
- Accuracy 2: 0.3084

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
- lr_scheduler_warmup_steps: 150
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Accuracy 0 | Accuracy 1 | Accuracy 2 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:----------:|:----------:|:----------:|
| No log        | 1.0   | 481  | 0.7431          | 0.4152   | 0.7707     | 0.1805     | 0.3650     |
| No log        | 2.0   | 962  | 0.7346          | 0.4152   | 0.8010     | 0.2190     | 0.2774     |
| No log        | 3.0   | 1443 | 0.7667          | 0.4162   | 0.8145     | 0.1895     | 0.3084     |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu113
- Datasets 2.1.0
- Tokenizers 0.11.6
