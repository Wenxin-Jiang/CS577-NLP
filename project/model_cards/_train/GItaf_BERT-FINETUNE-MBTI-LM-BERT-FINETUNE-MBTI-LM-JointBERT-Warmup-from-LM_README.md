---
tags:
- generated_from_trainer
model-index:
- name: BERT-FINETUNE-MBTI-LM-BERT-FINETUNE-MBTI-LM-JointBERT-Warmup-from-LM
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT-FINETUNE-MBTI-LM-BERT-FINETUNE-MBTI-LM-JointBERT-Warmup-from-LM

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.7966
- Cls loss: 1.4255
- Lm loss: 4.4398
- Cls Accuracy: 0.6380
- Cls F1: 0.6319
- Cls Precision: 0.6416
- Cls Recall: 0.6380
- Perplexity: 84.76

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 5.3087        | 1.0   | 3470  | 4.9005          | 1.4109   | 4.5474  | 0.6075       | 0.5981 | 0.6132        | 0.6075     | 94.39      |
| 4.8274        | 2.0   | 6940  | 4.7987          | 1.3448   | 4.4621  | 0.6242       | 0.6193 | 0.6381        | 0.6242     | 86.67      |
| 4.6472        | 3.0   | 10410 | 4.7966          | 1.4255   | 4.4398  | 0.6380       | 0.6319 | 0.6416        | 0.6380     | 84.76      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1