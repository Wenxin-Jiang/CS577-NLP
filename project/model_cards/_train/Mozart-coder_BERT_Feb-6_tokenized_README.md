---
tags:
- generated_from_trainer
model-index:
- name: BERT_Feb-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_Feb-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0043

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0575        | 1.0   | 265  | 0.0237          |
| 0.02          | 2.0   | 530  | 0.0131          |
| 0.0123        | 3.0   | 795  | 0.0086          |
| 0.0103        | 4.0   | 1060 | 0.0071          |
| 0.0078        | 5.0   | 1325 | 0.0061          |
| 0.007         | 6.0   | 1590 | 0.0047          |
| 0.006         | 7.0   | 1855 | 0.0035          |
| 0.006         | 8.0   | 2120 | 0.0043          |
| 0.0051        | 9.0   | 2385 | 0.0043          |
| 0.0057        | 10.0  | 2650 | 0.0038          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
