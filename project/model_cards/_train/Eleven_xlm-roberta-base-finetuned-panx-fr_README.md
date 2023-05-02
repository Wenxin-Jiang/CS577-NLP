---
license: mit
tags:
- generated_from_trainer
datasets:
- xtreme
metrics:
- f1
model-index:
- name: xlm-roberta-base-finetuned-panx-fr
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: xtreme
      type: xtreme
      args: PAN-X.fr
    metrics:
    - name: F1
      type: f1
      value: 0.835464333781965
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-panx-fr

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the xtreme dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2867
- F1: 0.8355

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
| 0.5817        | 1.0   | 191  | 0.3395          | 0.7854 |
| 0.2617        | 2.0   | 382  | 0.2856          | 0.8278 |
| 0.1708        | 3.0   | 573  | 0.2867          | 0.8355 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
