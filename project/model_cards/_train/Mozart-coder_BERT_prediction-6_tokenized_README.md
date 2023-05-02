---
tags:
- generated_from_trainer
model-index:
- name: BERT_prediction-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_prediction-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0326

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
| 0.0646        | 1.0   | 276  | 0.0370          |
| 0.0386        | 2.0   | 552  | 0.0348          |
| 0.0358        | 3.0   | 828  | 0.0336          |
| 0.0363        | 4.0   | 1104 | 0.0333          |
| 0.0357        | 5.0   | 1380 | 0.0334          |
| 0.0341        | 6.0   | 1656 | 0.0342          |
| 0.0342        | 7.0   | 1932 | 0.0341          |
| 0.0339        | 8.0   | 2208 | 0.0333          |
| 0.0332        | 9.0   | 2484 | 0.0344          |
| 0.0345        | 10.0  | 2760 | 0.0323          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
