---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- germanquad
model-index:
- name: jobBERTA_german_QA
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# jobBERTA_german_QA

This model is a fine-tuned version of [Joblift/distilbert-base-german-cased-finetuned-jl](https://huggingface.co/Joblift/distilbert-base-german-cased-finetuned-jl) on the germanquad dataset.

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu102
- Datasets 2.8.0
- Tokenizers 0.13.2
