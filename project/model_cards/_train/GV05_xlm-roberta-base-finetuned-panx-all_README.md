---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: xlm-roberta-base-finetuned-panx-all
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-panx-all

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1738
- F1: 0.8521

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
| 0.3082        | 1.0   | 835  | 0.1966          | 0.8029 |
| 0.1583        | 2.0   | 1670 | 0.1722          | 0.8403 |
| 0.1008        | 3.0   | 2505 | 0.1738          | 0.8521 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
