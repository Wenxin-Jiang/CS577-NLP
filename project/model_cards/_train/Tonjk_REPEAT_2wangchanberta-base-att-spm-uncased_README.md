---
tags:
- generated_from_trainer
model-index:
- name: REPEAT_2wangchanberta-base-att-spm-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# REPEAT_2wangchanberta-base-att-spm-uncased

This model is a fine-tuned version of [airesearch/wangchanberta-base-att-spm-uncased](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6799

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
| 0.4629        | 1.0   | 8561  | 0.3364          |
| 0.2805        | 2.0   | 17122 | 0.3314          |
| 0.2266        | 3.0   | 25683 | 0.5343          |
| 0.1821        | 4.0   | 34244 | 0.6103          |
| 0.1598        | 5.0   | 42805 | 0.6799          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.13.0+cu116
- Datasets 1.17.0
- Tokenizers 0.10.3
