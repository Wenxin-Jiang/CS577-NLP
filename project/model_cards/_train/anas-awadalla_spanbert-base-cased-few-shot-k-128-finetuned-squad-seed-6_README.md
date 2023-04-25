---
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: spanbert-base-cased-few-shot-k-128-finetuned-squad-seed-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# spanbert-base-cased-few-shot-k-128-finetuned-squad-seed-6

This model is a fine-tuned version of [SpanBERT/spanbert-base-cased](https://huggingface.co/SpanBERT/spanbert-base-cased) on the squad dataset.

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- training_steps: 200

### Training results



### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.17.0
- Tokenizers 0.10.3
