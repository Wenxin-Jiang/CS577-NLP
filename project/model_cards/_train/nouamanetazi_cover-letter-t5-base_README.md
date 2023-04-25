---
language: en
license: apache-2.0
tags:
- generated_from_trainer
- t5-base
model-index:
- name: cover-letter-t5-base
  results: []
widget:
- text: "coverletter name: Nouamane Tazi job: Machine Learning Engineer at HuggingFace background: Master's student in AI at the University of Paris Saclay experiences: I participated in the Digital Tech Year program, developing three minimal valuable products for three companies in a 7-week constraint. I also spent 1 year as a machine learning engineer for Flashbrand where I mainly worked on their chatbot . And I recently completed the HuggingFace course, where I built an amazing huggingface space. I am a strong team player."
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# cover-letter-t5-base

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on cover letter samples scraped from Indeed and JobHero.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
