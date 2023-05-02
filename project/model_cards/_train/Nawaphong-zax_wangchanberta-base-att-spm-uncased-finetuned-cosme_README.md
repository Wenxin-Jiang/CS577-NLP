---
tags:
- generated_from_trainer
model-index:
- name: wangchanberta-base-att-spm-uncased-finetuned-cosme
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wangchanberta-base-att-spm-uncased-finetuned-cosme

This model is a fine-tuned version of [airesearch/wangchanberta-base-att-spm-uncased](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9973

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
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.1386        | 1.0   | 391  | 1.9939          |
| 2.1301        | 2.0   | 782  | 1.9974          |
| 2.1296        | 3.0   | 1173 | 2.0013          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.11.0+cu113
- Datasets 1.17.0
- Tokenizers 0.10.3
