---
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: albert_gpt2_Full_summarization_cnndm
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert_gpt2_Full_summarization_cnndm

This model is a fine-tuned version of [](https://huggingface.co/) on the cnn_dailymail dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.12.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
