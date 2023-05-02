---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wmt14
model-index:
- name: opus-mt-de-en-finetuned-de-to-en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-de-en-finetuned-de-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-de-en](https://huggingface.co/Helsinki-NLP/opus-mt-de-en) on the wmt14 dataset.
It achieves the following results on the evaluation set:
- eval_loss: 1.3411
- eval_bleu: 32.4395
- eval_gen_len: 29.6925
- eval_runtime: 2250.0489
- eval_samples_per_second: 19.998
- eval_steps_per_second: 0.625
- epoch: 3.0
- step: 4221

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-06
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 11
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.19.2
- Pytorch 1.7.1+cu110
- Datasets 2.2.2
- Tokenizers 0.12.1
