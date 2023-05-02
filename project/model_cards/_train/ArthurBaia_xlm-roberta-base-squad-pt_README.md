---
license: mit
tags:
- generated_from_trainer
datasets:
- squad_v1_pt
model-index:
- name: xlm-roberta-base-squad-pt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-squad-pt

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the squad_v1_pt dataset.

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- distributed_type: tpu
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

- "epoch": 3.0,
- "eval_exact_match": 44.45600756859035,
- "eval_f1": 57.37953911779836,
- "eval_samples": 11095



### Framework versions

- Transformers 4.21.0.dev0
- Pytorch 1.9.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1