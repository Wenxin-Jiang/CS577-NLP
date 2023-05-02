---
tags:
- generated_from_trainer
model-index:
- name: BERT_Dec-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_Dec-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0372

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
| 0.0625        | 1.0   | 273  | 0.0376          |
| 0.039         | 2.0   | 546  | 0.0375          |
| 0.0385        | 3.0   | 819  | 0.0358          |
| 0.0375        | 4.0   | 1092 | 0.0380          |
| 0.0374        | 5.0   | 1365 | 0.0387          |
| 0.0358        | 6.0   | 1638 | 0.0378          |
| 0.0363        | 7.0   | 1911 | 0.0381          |
| 0.0373        | 8.0   | 2184 | 0.0377          |
| 0.0362        | 9.0   | 2457 | 0.0373          |
| 0.037         | 10.0  | 2730 | 0.0380          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
