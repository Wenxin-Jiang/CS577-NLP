---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BERT_MC_OpenBookQA_w_wrong_context
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_MC_OpenBookQA_w_wrong_context

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7450
- Accuracy: 0.922

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 11

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.3525        | 1.0   | 1859  | 0.2696          | 0.906    |
| 0.2084        | 2.0   | 3718  | 0.3284          | 0.9143   |
| 0.1263        | 3.0   | 5577  | 0.4205          | 0.9143   |
| 0.0734        | 4.0   | 7436  | 0.4688          | 0.9203   |
| 0.0437        | 5.0   | 9295  | 0.6266          | 0.9173   |
| 0.0357        | 6.0   | 11154 | 0.6934          | 0.9207   |
| 0.0264        | 7.0   | 13013 | 0.6947          | 0.92     |
| 0.0098        | 8.0   | 14872 | 0.6800          | 0.9197   |
| 0.0104        | 9.0   | 16731 | 0.7393          | 0.923    |
| 0.0067        | 10.0  | 18590 | 0.7846          | 0.9217   |
| 0.0034        | 11.0  | 20449 | 0.7450          | 0.922    |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.11.0
