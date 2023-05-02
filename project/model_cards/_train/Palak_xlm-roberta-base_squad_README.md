---
license: mit
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: xlm-roberta-base_squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base_squad

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the squad dataset.
- "eval_exact_match": 82.69631031220435
- "eval_f1": 89.4562841806503
- "eval_samples": 10918

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.14.1
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.10.3
