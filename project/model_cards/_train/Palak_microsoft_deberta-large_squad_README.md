---
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: microsoft-deberta-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# microsoft-deberta-large

This model is a fine-tuned version of [microsoft_deberta-large](https://huggingface.co/microsoft/deberta-large) on the **squadV1** dataset.

- "eval_exact_match": 87.89025543992432
- "eval_f1": 93.8755152147345
- "eval_samples": 10788

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 12
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Framework versions

- Transformers 4.14.1
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.10.3
