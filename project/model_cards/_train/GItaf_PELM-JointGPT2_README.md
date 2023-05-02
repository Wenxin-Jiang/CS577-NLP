---
tags:
- generated_from_trainer
model-index:
- name: PELM-JointGPT2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PELM-JointGPT2

This model is based on PELM framework and initialised from [genGPT-2](https://huggingface.co/GItaf/GPT2-LM-Finetuned-MBTI), then fine-tuned on the [MBTI dataset](https://www.kaggle.com/datasets/datasnaek/mbti-type).
It achieves the following results on the evaluation set:
- Loss: 4.3556
- Cls loss: 1.5778
- Lm loss: 3.9609
- Cls Accuracy: 0.6202
- Cls F1: 0.6126
- Cls Precision: 0.6216
- Cls Recall: 0.6202
- Perplexity: 52.50

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
| 4.2735        | 1.0   | 3470  | 4.3562          | 1.5844   | 3.9598  | 0.5833       | 0.5708 | 0.5928        | 0.5833     | 52.45      |
| 4.0754        | 2.0   | 6940  | 4.3295          | 1.4806   | 3.9590  | 0.6196       | 0.6113 | 0.6332        | 0.6196     | 52.41      |
| 3.985         | 3.0   | 10410 | 4.3556          | 1.5778   | 3.9609  | 0.6202       | 0.6126 | 0.6216        | 0.6202     | 52.50      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1