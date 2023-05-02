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
      config: PAN-X.en
      split: train
      args: PAN-X.en
    metrics:
    - name: F1
      type: f1
      value: 0.6886160714285715
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-panx-en

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the xtreme dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4043
- F1: 0.6886

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
| 1.1347        | 1.0   | 50   | 0.5771          | 0.4880 |
| 0.5066        | 2.0   | 100  | 0.4209          | 0.6582 |
| 0.3631        | 3.0   | 150  | 0.4043          | 0.6886 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
