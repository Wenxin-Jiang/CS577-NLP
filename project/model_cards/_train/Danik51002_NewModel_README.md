---
tags:
- generated_from_trainer
model-index:
- name: NewModel
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NewModel

This model is a fine-tuned version of [sberbank-ai/rugpt3small_based_on_gpt2](https://huggingface.co/sberbank-ai/rugpt3small_based_on_gpt2) on an unknown dataset.

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
- train_batch_size: 42
- eval_batch_size: 42
- seed: 42
- gradient_accumulation_steps: 20
- total_train_batch_size: 840
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 15
- num_epochs: 200

### Training results



### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Tokenizers 0.11.6
