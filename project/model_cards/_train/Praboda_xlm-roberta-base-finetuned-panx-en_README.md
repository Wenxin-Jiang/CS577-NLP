---
license: mit
tags:
- generated_from_trainer
datasets:
- xtreme
metrics:
- f1
model-index:
- name: xlm-roberta-base-finetuned-panx-en
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: xtreme
      type: xtreme
      args: PAN-X.en
    metrics:
    - name: F1
      type: f1
      value: 0.6991051454138703
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-panx-en

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the xtreme dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3926
- F1: 0.6991

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.1415        | 1.0   | 50   | 0.5404          | 0.5163 |
| 0.5045        | 2.0   | 100  | 0.4347          | 0.6498 |
| 0.371         | 3.0   | 150  | 0.3926          | 0.6991 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.13.0+cu116
- Datasets 1.16.1
- Tokenizers 0.10.3
