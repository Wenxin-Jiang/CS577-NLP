---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- syssr_en_ar
model-index:
- name: opus-mt-en-ar-finetuned-Math-13-10-en-to-ar
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-en-ar-finetuned-Math-13-10-en-to-ar

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ar](https://huggingface.co/Helsinki-NLP/opus-mt-en-ar) on the syssr_en_ar dataset.

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.13.0
- Tokenizers 0.10.3
