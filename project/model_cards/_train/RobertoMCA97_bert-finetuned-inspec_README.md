---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- inspec
metrics:
- f1
model-index:
- name: bert-finetuned-inspec
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: inspec
      type: inspec
      args: extraction
    metrics:
    - name: F1
      type: f1
      value: 0.30353331752430635
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-inspec

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the inspec dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3055
- F1: 0.3035

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.3323        | 1.0   | 125  | 0.2799          | 0.1521 |
| 0.2563        | 2.0   | 250  | 0.2638          | 0.2230 |
| 0.2179        | 3.0   | 375  | 0.2689          | 0.2607 |
| 0.1809        | 4.0   | 500  | 0.2807          | 0.3122 |
| 0.1545        | 5.0   | 625  | 0.3055          | 0.3035 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
