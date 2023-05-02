---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-cased-wikitext2-test-mlm
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-wikitext2-test-mlm

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 7.125

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: IPU
- gradient_accumulation_steps: 64
- total_train_batch_size: 256
- total_eval_batch_size: 20
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10
- training precision: Mixed Precision

### Training results



### Framework versions

- Transformers 4.20.0
- Pytorch 1.10.0+rocm4.2
- Datasets 2.3.2
- Tokenizers 0.12.1
