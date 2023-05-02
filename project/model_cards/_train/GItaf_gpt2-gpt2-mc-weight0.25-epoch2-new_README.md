---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-mc-weight0.25-epoch2-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-mc-weight0.25-epoch2-new

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.3629
- Cls loss: 1.4483
- Lm loss: 4.0006
- Cls Accuracy: 0.6023
- Cls F1: 0.5950
- Cls Precision: 0.6174
- Cls Recall: 0.6023
- Perplexity: 54.63

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Cls loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Lm loss | Perplexity | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:------------:|:------:|:-------------:|:----------:|:-------:|:----------:|:---------------:|
| 4.674         | 1.0   | 3470 | 1.5961   | 0.5487       | 0.5279 | 0.5643        | 0.5487     | 4.0380  | 56.71      | 4.4372          |
| 4.3809        | 2.0   | 6940 | 1.4483   | 0.6023       | 0.5950 | 0.6174        | 0.6023     | 4.0006  | 54.63      | 4.3629          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
