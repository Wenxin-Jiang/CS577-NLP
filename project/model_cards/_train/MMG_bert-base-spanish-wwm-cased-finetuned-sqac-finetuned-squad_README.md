---
tags:
- generated_from_trainer
datasets:
- squad_es
model-index:
- name: bert-base-spanish-wwm-cased-finetuned-sqac-finetuned-squad
  results: []
language:
- es
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-spanish-wwm-cased-finetuned-sqac-finetuned-squad

This model is a fine-tuned version of [MMG/bert-base-spanish-wwm-cased-finetuned-sqac](https://huggingface.co/MMG/bert-base-spanish-wwm-cased-finetuned-sqac) on the squad_es dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5325
- {'exact_match': 60.30274361400189, 'f1': 77.01962587890856}


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
- num_epochs: 3

### Training results

### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
