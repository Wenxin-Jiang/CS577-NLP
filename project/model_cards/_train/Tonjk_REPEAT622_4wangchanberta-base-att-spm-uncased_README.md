---
tags:
- generated_from_trainer
model-index:
- name: REPEAT622_4wangchanberta-base-att-spm-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# REPEAT622_4wangchanberta-base-att-spm-uncased

This model is a fine-tuned version of [airesearch/wangchanberta-base-att-spm-uncased](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1801

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.4095        | 1.0   | 9531  | 0.1991          |
| 0.2703        | 2.0   | 19062 | 0.2462          |
| 0.2166        | 3.0   | 28593 | 0.1892          |
| 0.1714        | 4.0   | 38124 | 0.1808          |
| 0.1637        | 5.0   | 47655 | 0.1801          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.13.0+cu116
- Datasets 1.17.0
- Tokenizers 0.10.3
