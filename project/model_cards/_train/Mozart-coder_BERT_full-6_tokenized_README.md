---
tags:
- generated_from_trainer
model-index:
- name: BERT_full-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_full-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0362

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
- num_epochs: 25
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0775        | 1.0   | 284  | 0.0411          |
| 0.0428        | 2.0   | 568  | 0.0393          |
| 0.0395        | 3.0   | 852  | 0.0396          |
| 0.0395        | 4.0   | 1136 | 0.0374          |
| 0.0379        | 5.0   | 1420 | 0.0379          |
| 0.037         | 6.0   | 1704 | 0.0399          |
| 0.0368        | 7.0   | 1988 | 0.0382          |
| 0.0378        | 8.0   | 2272 | 0.0378          |
| 0.0365        | 9.0   | 2556 | 0.0362          |
| 0.0374        | 10.0  | 2840 | 0.0359          |
| 0.0372        | 11.0  | 3124 | 0.0373          |
| 0.0358        | 12.0  | 3408 | 0.0378          |
| 0.0361        | 13.0  | 3692 | 0.0385          |
| 0.0364        | 14.0  | 3976 | 0.0383          |
| 0.035         | 15.0  | 4260 | 0.0376          |
| 0.035         | 16.0  | 4544 | 0.0376          |
| 0.036         | 17.0  | 4828 | 0.0388          |
| 0.0365        | 18.0  | 5112 | 0.0372          |
| 0.0355        | 19.0  | 5396 | 0.0363          |
| 0.0349        | 20.0  | 5680 | 0.0378          |
| 0.0345        | 21.0  | 5964 | 0.0377          |
| 0.0349        | 22.0  | 6248 | 0.0372          |
| 0.035         | 23.0  | 6532 | 0.0374          |
| 0.0351        | 24.0  | 6816 | 0.0379          |
| 0.0351        | 25.0  | 7100 | 0.0374          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
