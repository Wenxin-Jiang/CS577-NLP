---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-mc-weight0.25-epoch2-new-nosharing
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-mc-weight0.25-epoch2-new-nosharing

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.3672
- Cls loss: 1.4634
- Lm loss: 4.0012
- Cls Accuracy: 0.6121
- Cls F1: 0.6023
- Cls Precision: 0.6288
- Cls Recall: 0.6121
- Perplexity: 54.66

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
| 4.6729        | 1.0   | 3470 | 1.5425   | 0.5689       | 0.5448 | 0.5732        | 0.5689     | 4.0392  | 56.78      | 4.4248          |
| 4.3854        | 2.0   | 6940 | 1.4634   | 0.6121       | 0.6023 | 0.6288        | 0.6121     | 4.0012  | 54.66      | 4.3672          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
