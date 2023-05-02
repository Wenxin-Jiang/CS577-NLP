---
tags:
- generated_from_trainer
model-index:
- name: BERT-FINETUNE-MBTI-CLS-BERT-FINETUNE-MBTI-CLS-JointBERT-Warmup-from-CLS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT-FINETUNE-MBTI-CLS-BERT-FINETUNE-MBTI-CLS-JointBERT-Warmup-from-CLS

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.3549
- Cls loss: 2.1311
- Lm loss: 4.8216
- Cls Accuracy: 0.6058
- Cls F1: 0.6037
- Cls Precision: 0.6084
- Cls Recall: 0.6058
- Perplexity: 124.17

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
| 5.778         | 1.0   | 3470  | 5.5656          | 1.9246   | 5.0840  | 0.5931       | 0.5907 | 0.5968        | 0.5931     | 161.43     |
| 5.1443        | 2.0   | 6940  | 5.3831          | 2.0178   | 4.8783  | 0.6069       | 0.6057 | 0.6177        | 0.6069     | 131.40     |
| 4.9386        | 3.0   | 10410 | 5.3549          | 2.1311   | 4.8216  | 0.6058       | 0.6037 | 0.6084        | 0.6058     | 124.17     |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1