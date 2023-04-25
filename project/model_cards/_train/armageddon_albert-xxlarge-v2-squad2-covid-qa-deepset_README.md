---
tags:
- generated_from_trainer
datasets:
- covid_qa_deepset
model-index:
- name: albert-xxlarge-v2-squad2-covid-qa-deepset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-xxlarge-v2-squad2-covid-qa-deepset

This model is a fine-tuned version of [mfeb/albert-xxlarge-v2-squad2](https://huggingface.co/mfeb/albert-xxlarge-v2-squad2) on the covid_qa_deepset dataset.

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
- distributed_type: tpu
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results



### Framework versions

- Transformers 4.16.2
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
