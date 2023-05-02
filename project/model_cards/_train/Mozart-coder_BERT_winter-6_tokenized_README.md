---
tags:
- generated_from_trainer
model-index:
- name: BERT_winter-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_winter-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0361

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
| 0.0706        | 1.0   | 262  | 0.0369          |
| 0.0388        | 2.0   | 524  | 0.0374          |
| 0.037         | 3.0   | 786  | 0.0363          |
| 0.0372        | 4.0   | 1048 | 0.0374          |
| 0.0376        | 5.0   | 1310 | 0.0351          |
| 0.0366        | 6.0   | 1572 | 0.0351          |
| 0.0377        | 7.0   | 1834 | 0.0373          |
| 0.0373        | 8.0   | 2096 | 0.0370          |
| 0.0358        | 9.0   | 2358 | 0.0359          |
| 0.0364        | 10.0  | 2620 | 0.0382          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
