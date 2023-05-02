---
tags:
- translation
metrics:
- bleu
model-index:
- name: mbart50-finetuned-multi30-en-to-de
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart50-finetuned-multi30-en-to-de

This model is a fine-tuned version of [facebook/mbart-large-50-one-to-many-mmt](https://huggingface.co/facebook/mbart-large-50-one-to-many-mmt) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5946
- Bleu: 48.2650

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0+cu113
- Datasets 2.2.2
- Tokenizers 0.10.3
