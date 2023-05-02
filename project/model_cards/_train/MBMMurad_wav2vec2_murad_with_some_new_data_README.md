---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cvbn
model-index:
- name: wav2vec2_murad_with_some_new_data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2_murad_with_some_new_data

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the cvbn dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2971
- eval_wer: 0.2084
- eval_runtime: 511.5492
- eval_samples_per_second: 9.774
- eval_steps_per_second: 0.612
- epoch: 26.88
- step: 33600

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.21.1
- Pytorch 1.11.0+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1
