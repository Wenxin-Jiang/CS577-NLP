---
tags:
- generated_from_trainer
model-index:
- name: BERT_full_data3-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_full_data3-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0370

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
| 0.0649        | 1.0   | 284  | 0.0381          |
| 0.0401        | 2.0   | 568  | 0.0364          |
| 0.0374        | 3.0   | 852  | 0.0371          |
| 0.0371        | 4.0   | 1136 | 0.0352          |
| 0.0365        | 5.0   | 1420 | 0.0360          |
| 0.0353        | 6.0   | 1704 | 0.0375          |
| 0.0353        | 7.0   | 1988 | 0.0357          |
| 0.0364        | 8.0   | 2272 | 0.0349          |
| 0.0353        | 9.0   | 2556 | 0.0343          |
| 0.0356        | 10.0  | 2840 | 0.0345          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
