---
tags:
- generated_from_trainer
model-index:
- name: nllb-200-distilled-600M-finetuned-pan_Guru-to-eng_Latn-finetuned-pan_Guru-to-eng_Latn_extratrain
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# nllb-200-distilled-600M-finetuned-pan_Guru-to-eng_Latn-finetuned-pan_Guru-to-eng_Latn_extratrain

This model was trained from scratch on the None dataset.

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
