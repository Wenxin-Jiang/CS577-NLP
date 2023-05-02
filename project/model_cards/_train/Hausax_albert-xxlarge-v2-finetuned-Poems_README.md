---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: albert-xxlarge-v2-finetuned-Poems
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-xxlarge-v2-finetuned-Poems

This model is a fine-tuned version of [albert-xxlarge-v2](https://huggingface.co/albert-xxlarge-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1923

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-07
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.482         | 1.0   | 19375 | 2.2959          |
| 2.258         | 2.0   | 38750 | 2.2357          |
| 2.2146        | 3.0   | 58125 | 2.2085          |
| 2.1975        | 4.0   | 77500 | 2.1929          |
| 2.1893        | 5.0   | 96875 | 2.1863          |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
