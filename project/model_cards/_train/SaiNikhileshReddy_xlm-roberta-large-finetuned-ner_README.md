---
license: mit
tags:
- generated_from_trainer
datasets:
- hi_ner_config
model-index:
- name: xlm-roberta-large-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-finetuned-ner

This model is a fine-tuned version of [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) on the hi_ner_config dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2329
- eval_precision: 0.7110
- eval_recall: 0.6854
- eval_f1: 0.6980
- eval_accuracy: 0.9332
- eval_runtime: 162.3478
- eval_samples_per_second: 66.9
- eval_steps_per_second: 16.73
- epoch: 2.64
- step: 50198

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
