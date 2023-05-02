---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: xlm-roberta-large-finetuned-ours-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-finetuned-ours-DS

This model is a fine-tuned version of [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9568
- Accuracy: 0.71
- Precision: 0.6689
- Recall: 0.6607
- F1: 0.6637

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.6820964947491663e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9953        | 1.99  | 199  | 0.7955          | 0.66     | 0.7533    | 0.5971 | 0.5352 |
| 0.6638        | 3.98  | 398  | 0.8043          | 0.735    | 0.7068    | 0.6782 | 0.6846 |
| 0.3457        | 5.97  | 597  | 0.9568          | 0.71     | 0.6689    | 0.6607 | 0.6637 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
